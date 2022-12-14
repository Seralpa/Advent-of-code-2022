import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	lines = [[tuple(map(int, p.split(","))) for p in l.split(" -> ")] for l in f.read().splitlines()]

right_padding = 0  #increase if sand overflows to the right
maxj = max([max(l, key=lambda x: x[0])[0] for l in lines]) + 1 + right_padding
maxi = max([max(l, key=lambda x: x[1])[1] for l in lines]) + 1

cave = [["." for _ in range(maxj)] for _ in range(maxi)]
for l in lines:
	for (p1j, p1i), (p2j, p2i) in zip(l, l[1:]):
		for i in range(min(p1i, p2i), max(p1i, p2i) + 1):
			for j in range(min(p1j, p2j), max(p1j, p2j) + 1):
				cave[i][j] = "#"

finish = False
while not finish:
	sand = (0, 500)
	while True:
		if sand[0] + 1 == len(cave):
			finish = True
			break
		if cave[sand[0] + 1][sand[1]] == ".":
			sand = (sand[0] + 1, sand[1])
		elif cave[sand[0] + 1][sand[1] - 1] == ".":
			sand = (sand[0] + 1, sand[1] - 1)
		elif cave[sand[0] + 1][sand[1] + 1] == ".":
			sand = (sand[0] + 1, sand[1] + 1)
		else:
			cave[sand[0]][sand[1]] = "O"
			break

print(sum(r.count("O") for r in cave))