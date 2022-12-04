import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	pair_assignments = [map(int, l.split(',')) for l in f.read().replace('-', ',').splitlines()]

count = 0
for a1_start, a1_end, a2_start, a2_end in pair_assignments:
	r1 = set(range(a1_start, a1_end + 1))
	r2 = set(range(a2_start, a2_end + 1))
	if len(r1 & r2) > 0:
		count += 1
print(count)