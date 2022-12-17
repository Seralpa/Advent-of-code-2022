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


def simulate(cave: set, rocks: list[Rock], n: int, h_cycle1=-1, h_cycle2=-1) -> tuple[int, int, int]:
	height = 0
	j = 0
	cycle1, cycle2 = -1, -1
	for i in range(n):
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
				if height == h_cycle1:
					cycle1 = i + 1
				if height == h_cycle2:
					cycle2 = i + 1
				break
			r = new_r
	return height, cycle1, cycle2


def get_cycle_height(rocks: list[Rock], cycle1: int, cycle2: int) -> int:
	return simulate(set(), rocks, cycle2)[0] - simulate(set(), rocks, cycle1)[0]


def print_cave(cave: set[tuple[int, int]], height: int):
	for i in reversed(range(height + 1)):
		for j in range(7):
			print("#" if (i, j) in cave else ".", end="")
		# print(f" {i}", end="")
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
# to get h_cycle1 and h_cycle2 print tower and manually check when repetitions start
height, cycle1, cycle2 = simulate(cave, rocks, 3000, h_cycle1=933, h_cycle2=3670)
# print_cave(cave, height)

total_stones = 1000000000000
stones_per_cycle = cycle2 - cycle1
num_cycles = (total_stones - cycle1) // stones_per_cycle
rest = ((total_stones - cycle1) % stones_per_cycle) + cycle1
total_height = (num_cycles * get_cycle_height(rocks, cycle1, cycle2)) + simulate(set(), rocks, rest)[0]
print(total_height)