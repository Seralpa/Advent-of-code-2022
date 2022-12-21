import os
import sympy

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l.split(": ") for l in f.read().splitlines()]

monkeys = dict()
for m, val in data:
	monkeys[m] = ["("] + val.split(" ") + [")"]

monkeys["humn"] = ["X"]
monkeys["root"][2] = "-"

mod = True
while mod:
	mod = False
	for i, n in enumerate(monkeys["root"]):
		if n not in monkeys.keys():
			continue
		monkeys["root"] = monkeys["root"][:i] + monkeys[n] + monkeys["root"][i + 1:]
		mod = True
		break

print(sympy.solve(sympy.sympify("".join(monkeys["root"])))[0])