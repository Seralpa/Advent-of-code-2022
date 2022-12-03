import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	rucksacks = [l for l in f.read().splitlines()]

prio = 0
for i in range(0, len(rucksacks), 3):
	r1 = set(rucksacks[i + 0])
	r2 = set(rucksacks[i + 1])
	r3 = set(rucksacks[i + 2])
	item = list(r1 & r2 & r3)[0]
	if ord(item) >= ord("a") and ord(item) <= ord("z"):
		prio += ord(item) - ord('a') + 1
	else:
		prio += ord(item) - ord('A') + 27
print(prio)