import os
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l for l in f.read().splitlines()]

convert = {"-": -1, "=": -2}

count = 0
for num in data:
	count += sum([(convert[c] if c in "-=" else int(c)) * 5**i for i, c in enumerate(reversed(num))])

count = list(reversed(str(np.base_repr(count, base=5))))
overflow = False
for i, c in enumerate(count):
	if c in "012":
		continue
	if c == "3":
		count[i] = "="
	elif c == "4":
		count[i] = "-"
	elif c == "5":
		count[i] = "0"
	if i == 0:
		count.append("0")
	count[i + 1] = str(int(count[i + 1]) + 1)
print("".join(reversed(count)))