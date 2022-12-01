import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [sum([int(n) for n in l.splitlines()]) for l in f.read().split("\n\n")]
print(max(data))
