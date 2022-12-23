from collections import Counter
import os

Elf = tuple[int, int]

N = [(-1, -1), (-1, 0), (-1, 1)]
S = [(1, 1), (1, 0), (1, -1)]
W = [(-1, -1), (1, -1), (0, -1)]
E = [(-1, 1), (0, 1), (1, 1)]
dirs_8 = [N, S, W, E]
dirs_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def has_neighbours(elf: Elf, elves: set[Elf]) -> list[bool]:
	nswe = [False, False, False, False]
	for i, d in enumerate(dirs_8):
		for c in d:
			if (elf[0] + c[0], elf[1] + c[1]) in elves:
				nswe[i] = True
				break
	return nswe


def print_elves(elves: list[Elf]):
	for i in range(min(elves, key=lambda p: p[0])[0], max(elves, key=lambda p: p[0])[0] + 1):
		for j in range(min(elves, key=lambda p: p[1])[1], max(elves, key=lambda p: p[1])[1] + 1):
			print("#" if (i, j) in elves else ".", end="")
		print()
	print()


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	elves = [(i, j) for i, r in enumerate(f.read().splitlines()) for j, c in enumerate(r) if c == "#"]

dir_order = 0
r = 0
while True:
	proposals = []
	elves_set = set(elves)
	for i, elf in enumerate(elves):
		nswe = has_neighbours(elf, elves_set)
		if len([n for n in nswe if n]) == 0:
			continue
		for j in range(4):
			dir_id = (dir_order + j) % 4
			if not nswe[dir_id]:
				proposals.append((i, (elf[0] + dirs_4[dir_id][0], elf[1] + dirs_4[dir_id][1])))
				break

	cnt = Counter([p for _, p in proposals])
	proposals = [p for p in proposals if cnt[p[1]] == 1]

	for i, p in proposals:
		elves[i] = p
	dir_order = (dir_order + 1) % 4
	r += 1
	if len(proposals) == 0:
		print(r)
		break