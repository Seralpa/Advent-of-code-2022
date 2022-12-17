import os

Rock = frozenset[tuple[int, int]]


def shift_start(rock: Rock, height: int) -> frozenset[tuple[int, int]]:
	return frozenset(((i + height + 3, j + 2) for i, j in rock))


def shift(cave: set[tuple[int, int]], rock: Rock, direction: tuple[int, int]) -> Rock:
	new_rock = set()
	for i, j in rock:
		i += direction[0]
		j += direction[1]
		if (i, j) in cave or i <= 0 or j < 0 or j >= 7:
			return rock
		new_rock.add((i, j))
	return frozenset(new_rock)


def print_cave(cave: set[tuple[int, int]], height: int):
	for i in reversed(range(height + 1)):
		for j in range(7):
			print("#" if (i, j) in cave else ".", end="")
		print()


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l for l in f.read().strip()]

rocks: list[Rock] = []
rocks.append(frozenset({(0, 0), (0, 1), (0, 2), (0, 3)}))
rocks.append(frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}))
rocks.append(frozenset({(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)}))
rocks.append(frozenset({(0, 0), (1, 0), (2, 0), (3, 0)}))
rocks.append(frozenset({(0, 0), (1, 0), (1, 1), (0, 1)}))

cave = set()
height = 0
j = 0
for i in range(2022):
	r = shift_start(rocks[i % len(rocks)], height + 1)
	while True:
		if data[j] == ">":
			r = shift(cave, r, (0, 1))
		elif data[j] == "<":
			r = shift(cave, r, (0, -1))
		else:
			print("err")

		j = (j + 1) % len(data)
		new_r = shift(cave, r, (-1, 0))
		if new_r == r:
			cave.update(r)
			height = max(cave, key=lambda p: p[0])[0]
			break
		r = new_r
print(height)