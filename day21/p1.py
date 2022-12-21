import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l.split(": ") for l in f.read().replace("/", "//").splitlines()]

monkeys = dict()
for m, val in data:
	monkeys[m] = val.split(" ")

while len(monkeys["root"]) != 1:
	for m, v in monkeys.items():
		if len(v) == 1:
			continue
		if len(monkeys[v[0]]) == 1 and len(monkeys[v[2]]) == 1:
			v[0] = monkeys[v[0]][0]
			v[2] = monkeys[v[2]][0]
			monkeys[m] = [str(eval("".join(v)))]

print(monkeys["root"][0])