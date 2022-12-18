import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	lava = set([tuple(map(int, l.split(","))) for l in f.read().splitlines()])

total = 0
for x, y, z in lava:
	faces = 6
	if (x - 1, y, z) in lava:
		faces -= 1
	if (x + 1, y, z) in lava:
		faces -= 1
	if (x, y - 1, z) in lava:
		faces -= 1
	if (x, y + 1, z) in lava:
		faces -= 1
	if (x, y, z - 1) in lava:
		faces -= 1
	if (x, y, z + 1) in lava:
		faces -= 1
	total += faces
print(total)