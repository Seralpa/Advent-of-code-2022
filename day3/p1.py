import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	rucksacks = [l for l in f.read().splitlines()]

prio = 0
for r in rucksacks:
	comp_size = len(r) // 2
	c1, c2 = set(r[:comp_size]), set(r[comp_size:])
	item = list(c1 & c2)[0]
	if ord(item) >= ord("a") and ord(item) <= ord("z"):
		prio += ord(item) - ord('a') + 1
	else:
		prio += ord(item) - ord('A') + 27
print(prio)