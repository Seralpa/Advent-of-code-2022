from __future__ import annotations
from dataclasses import dataclass
import os
import math
from types import CodeType


@dataclass
class Monkey:
	items: list[int]
	op: CodeType
	test: int
	next_id: tuple[int, int]
	inspected: int = 0

	def process_items(self, monkeys: list[Monkey]):
		for i in self.items:
			self.inspected += 1
			i = eval(self.op) // 3
			next_id = self.next_id[0] if i % self.test == 0 else self.next_id[1]
			monkeys[next_id].items.append(i)
		self.items = []


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read().replace("Monkey ", "")
	data = data.replace("  Starting items: ", "")
	data = data.replace("  Operation: new = ", "")
	data = data.replace("  Test: divisible by ", "")
	data = data.replace("    If true: throw to monkey ", "")
	data = data.replace("    If false: throw to monkey ", "")
	data = data.replace(":", "").replace("old", "i")
	data = [l.splitlines() for l in data.split("\n\n")]

monkeys: list[Monkey] = []
for m in data:
	items = list(map(int, m[1].split(", ")))
	monkeys.append(Monkey(items, op=compile(m[2], "op", "eval"), test=int(m[3]), next_id=(int(m[4]), int(m[5]))))

for round in range(20):
	for m in monkeys:
		m.process_items(monkeys)

print(math.prod(sorted([m.inspected for m in monkeys])[-2:]))