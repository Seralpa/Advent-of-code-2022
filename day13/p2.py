from __future__ import annotations
from dataclasses import dataclass
import os
from typing import Optional
from functools import total_ordering


@total_ordering
@dataclass
class Packet:
	l: list

	def __lt__(self, __o: Packet) -> Optional[bool]:
		return in_order(self.l, __o.l)

	def __eq__(self, __o: Packet) -> bool:
		return self.l == __o.l


def in_order(left: list, right: list) -> Optional[bool]:
	for l, r in zip(left, right):
		if isinstance(r, int) and isinstance(l, int):
			if l == r:
				continue
			return l < r
		elif isinstance(r, int):
			res = in_order(l, [r])
		elif isinstance(l, int):
			res = in_order([l], r)
		else:
			res = in_order(l, r)
		if res != None:
			return res
	return None if len(left) == len(right) else len(left) < len(right)


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	packets = [Packet(eval(l)) for l in f.read().replace("\n\n", "\n").splitlines()]

divider1 = Packet([[2]])
divider2 = Packet([[6]])

packets.append(divider1)
packets.append(divider2)

packets.sort()
print((packets.index(divider1) + 1) * (packets.index(divider2) + 1))
