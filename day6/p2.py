import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read().strip()

window_size = 4
window = []
for i, c in enumerate(data):
	window.append(c)
	if len(window) <= window_size:
		continue
	window.pop(0)
	if len(set(window)) == window_size:
		print(i + 1)
		break
