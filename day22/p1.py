import os


def is_outside(board: list[list[str]], pos: tuple[int, int]) -> bool:
	return pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[pos[0]]) or board[pos[0]][pos[1]] == " "


def wrap_around(board: list[list[str]], pos: tuple[int, int], dir_idx: int) -> tuple[int, int]:
	op_dir = dirs[(dir_idx + 2) % len(dirs)]
	while True:
		new_pos = (pos[0] + op_dir[0], pos[1] + op_dir[1])
		if is_outside(board, new_pos):
			return pos
		pos = new_pos


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	board, instrucctions = f.read().split("\n\n")

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
			if is_outside(board, new_pos):
				new_pos = wrap_around(board, pos, dir_idx)
			if board[new_pos[0]][new_pos[1]] == "#":
				break
			pos = new_pos

print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + dir_idx)