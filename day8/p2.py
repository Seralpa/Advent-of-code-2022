import os
from typing import Iterable


def get_score(own_size: int, forest: list[list[int]], range_i: Iterable[int], range_j: Iterable[int]) -> int:
	count = 0
	for i in range_i:
		for j in range_j:
			count += 1
			if forest[i][j] >= own_size:
				return count
	return count


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	forest = [list(map(int, l)) for l in f.read().splitlines()]

max_score = 0
for i, r in enumerate(forest[1:-1], start=1):
	for j, tree in enumerate(r[1:-1], start=1):
		score = 1
		# up
		score *= get_score(tree, forest, reversed(range(0, i)), range(j, j + 1))
		# down
		score *= get_score(tree, forest, range(i + 1, len(forest)), range(j, j + 1))
		# left
		score *= get_score(tree, forest, range(i, i + 1), reversed(range(0, j)))
		# right
		score *= get_score(tree, forest, range(i, i + 1), range(j + 1, len(r)))
		if score > max_score:
			max_score = score
print(max_score)