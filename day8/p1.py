import os


def is_visible(own_size: int, forest: list[list[int]], range_i: range, range_j: range) -> bool:
	for i in range_i:
		for j in range_j:
			if forest[i][j] >= own_size:
				return False
	return True


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	forest = [list(map(int, l)) for l in f.read().splitlines()]

# count edges
visible = len(forest) * 2 + len(forest[1]) * 2 - 4
for i, r in enumerate(forest[1:-1], start=1):
	for j, tree in enumerate(r[1:-1], start=1):
		# up
		if is_visible(tree, forest, range(0, i), range(j, j + 1)):
			visible += 1
			continue
		# down
		if is_visible(tree, forest, range(i + 1, len(forest)), range(j, j + 1)):
			visible += 1
			continue
		# left
		if is_visible(tree, forest, range(i, i + 1), range(0, j)):
			visible += 1
			continue
		# right
		if is_visible(tree, forest, range(i, i + 1), range(j + 1, len(r))):
			visible += 1
			continue
print(visible)
