import os


def is_outside(board: list[list[str]], pos: tuple[int, int]) -> bool:
	return pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[pos[0]]) or board[pos[0]][pos[1]] == " "


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	board, instrucctions = f.read().split("\n\n")

# ESWN
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ins_list = []
curr_num = ""
for c in instrucctions:
	if c in "RL":
		if curr_num != "":
			ins_list.append(int(curr_num))
		curr_num = ""
		ins_list.append(c)
	else:
		curr_num += c
if curr_num != "":
	ins_list.append(int(curr_num))
board = [list(r) for r in board.splitlines()]

side = 50
wrap_dict = ({((0, j), 3): ((i2, 0), 0) for j, i2 in zip(range(side, 2 * side), range(3 * side, 4 * side))} |
             {(((4 * side) - 1, j), 1): ((0, j2), 1) for j, j2 in zip(range(0, side), range(2 * side, 3 * side))} |
             {(((3 * side) - 1, j), 1): ((i2, side - 1), 2) for j, i2 in zip(range(side, 2 * side), range(3 * side, 4 * side))} |
             {((i, (3 * side) - 1), 0): ((i2, (2 * side) - 1), 2) for i, i2 in zip(reversed(range(0, side)), range(2 * side, 3 * side))} |
             {((side - 1, j), 1): ((i2, (2 * side) - 1), 2) for j, i2 in zip(range(2 * side, 3 * side), range(side, 2 * side))} |
             {((i, side), 2): ((2 * side, j2), 1) for i, j2 in zip(range(side, 2 * side), range(0, side))} |
             {((i, 0), 2): ((i2, side), 0) for i, i2 in zip(range(2 * side, 3 * side), reversed(range(0, side)))})
aux = dict()
for k, v in wrap_dict.items():
	aux[v[0], (v[1] + 2) % 4] = (k[0], (k[1] + 2) % 4)
wrap_dict.update(aux)

dir_idx = 0
pos = (0, board[0].index("."))
for ins in ins_list:
	if ins == "R":
		dir_idx = (dir_idx + 1) % len(dirs)
	elif ins == "L":
		dir_idx = (dir_idx - 1) % len(dirs)
	else:
		for _ in range(ins):
			new_pos = (pos[0] + dirs[dir_idx][0], pos[1] + dirs[dir_idx][1])
			new_dir_idx = dir_idx
			if is_outside(board, new_pos):
				new_pos, new_dir_idx = wrap_dict[pos, dir_idx]
			if board[new_pos[0]][new_pos[1]] == "#":
				break
			pos = new_pos
			dir_idx = new_dir_idx

print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + dir_idx)