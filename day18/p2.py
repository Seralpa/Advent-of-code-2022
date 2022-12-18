import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	lava = set([tuple(map(int, l.split(","))) for l in f.read().splitlines()])

x_range = min(lava, key=lambda x: x[0])[0] - 1, max(lava, key=lambda x: x[0])[0] + 2
y_range = min(lava, key=lambda x: x[1])[1] - 1, max(lava, key=lambda x: x[1])[1] + 2
z_range = min(lava, key=lambda x: x[2])[2] - 1, max(lava, key=lambda x: x[2])[2] + 2

water = set([(x_range[0], y_range[0], z_range[0])])
checked = set()
faces = 0
old_faces = -1
while old_faces != faces:
	old_faces = faces
	for x in range(x_range[0], x_range[1]):
		for y in range(y_range[0], y_range[1]):
			for z in range(z_range[0], z_range[1]):
				if (x, y, z) not in water or (x, y, z) in checked:
					continue
				if (x - 1, y, z) in lava:
					faces += 1
				elif (x - 1, y, z) not in water:
					water.add((x - 1, y, z))
				if (x + 1, y, z) in lava:
					faces += 1
				elif (x + 1, y, z) not in water:
					water.add((x + 1, y, z))
				if (x, y - 1, z) in lava:
					faces += 1
				elif (x, y - 1, z) not in water:
					water.add((x, y - 1, z))
				if (x, y + 1, z) in lava:
					faces += 1
				elif (x, y + 1, z) not in water:
					water.add((x, y + 1, z))
				if (x, y, z - 1) in lava:
					faces += 1
				elif (x, y, z - 1) not in water:
					water.add((x, y, z - 1))
				if (x, y, z + 1) in lava:
					faces += 1
				elif (x, y, z + 1) not in water:
					water.add((x, y, z + 1))
				checked.add((x, y, z))
print(faces)