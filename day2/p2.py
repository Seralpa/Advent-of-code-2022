import os


def get_round_result(p1: int, p2: int) -> int:
	if p1 == p2:  # draw
		return 3
	if (p1 + 1) % 3 == p2:  # p2 win
		return 6
	return 0  # p1 win


def get_play(p1: int, res: int) -> int:
	if res == 0:  #loss
		return (p1 + 2) % 3
	if res == 1:  #draw
		return p1
	if res == 2:  #win
		return (p1 + 1) % 3


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l.split(' ') for l in f.read().splitlines()]

# 0 based to make modules easier
char2int = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}

score = 0
for round in data:
	p1, res = map(lambda x: char2int[x], round)
	p2 = get_play(p1, res)
	score += p2 + 1
	score += get_round_result(p1, p2)
print(score)