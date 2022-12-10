import os


def draw_pixel(crt: list[list[str]], i: int, j: int, x: int):
	crt[i][j] = "#" if abs(x - j) <= 1 else "."


def inc_crt_ptr(i: int, j: int) -> tuple[int, int]:
	nj = (j + 1) % 40
	ni = (i + 1) % 6 if nj == 0 else i
	return ni, nj


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	instructions = [l.split(' ') for l in f.read().splitlines()]

cycle = 0
x = 1
crt = [["." for _ in range(40)] for _ in range(6)]
i, j = 0, 0
for ins in instructions:
	match ins:
		case ["noop"]:
			cycle += 1
			draw_pixel(crt, i, j, x)
			i, j = inc_crt_ptr(i, j)
		case ["addx", num]:
			cycle += 2
			draw_pixel(crt, i, j, x)
			i, j = inc_crt_ptr(i, j)
			draw_pixel(crt, i, j, x)
			i, j = inc_crt_ptr(i,j)
			x += int(num)

for r in crt:
	print("".join(r))