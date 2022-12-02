import os


def get_round_result(p1: int, p2: int) -> int:
	if p1 == p2:  # draw
		return 3
	if (p1 + 1) % 3 == p2:  # p2 win
		return 6
	return 0  # p1 win


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	guide = [l.split(' ') for l in f.read().splitlines()]

# 0 based to make modules easier
char2int = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}

score = 0
for round in guide:
	p1, p2 = map(lambda x: char2int[x], round)
	score += p2 + 1
	score += get_round_result(p1, p2)
print(score)