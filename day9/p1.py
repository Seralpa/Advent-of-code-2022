import os


def move(curr: tuple, dir: tuple):
	return (curr[0] + dir[0], curr[1] + dir[1])


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	motions = [l.split() for l in f.read().splitlines()]

visited = set()
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
head = (0, 0)
tail = (0, 0)

for dir, n in motions:
	for _ in range(int(n)):
		visited.add(tail)
		head = move(head, directions[dir])
		# touching
		if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
			continue

		v = (head[0] > tail[0]) - (head[0] < tail[0])
		h = (head[1] > tail[1]) - (head[1] < tail[1])
		tail = move(tail, (v, h))

visited.add(tail)
print(len(visited))