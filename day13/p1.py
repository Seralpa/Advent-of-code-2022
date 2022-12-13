import os
from typing import Optional


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
	pairs = [tuple(map(eval, l.splitlines())) for l in f.read().split("\n\n")]

correct = []
for i, (left, right) in enumerate(pairs, start=1):
	if in_order(left, right) != False:
		correct.append(i)
print(sum(correct))