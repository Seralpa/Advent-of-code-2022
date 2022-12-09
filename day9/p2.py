import os


def move(curr: tuple, dir: tuple):
	return (curr[0] + dir[0], curr[1] + dir[1])


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	motions = [l.split() for l in f.read().splitlines()]

visited = set()
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
rope = [(0, 0) for _ in range(10)]

for dir, n in motions:
	for _ in range(int(n)):
		visited.add(rope[-1])
		rope[0] = move(rope[0], directions[dir])
		for i, knot in enumerate(rope[1:], start=1):
			# touching
			if abs(rope[i - 1][0] - knot[0]) <= 1 and abs(rope[i - 1][1] - knot[1]) <= 1:
				continue

			v = (rope[i - 1][0] > knot[0]) - (rope[i - 1][0] < knot[0])
			h = (rope[i - 1][1] > knot[1]) - (rope[i - 1][1] < knot[1])
			rope[i] = move(knot, (v, h))

visited.add(rope[-1])
print(len(visited))