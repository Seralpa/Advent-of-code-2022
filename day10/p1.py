import os


def get_cycle_value(cycle: int, x: int):
	if (cycle - 20) % 40 == 0:
		return x * cycle
	return 0


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	instructions = [l.split(' ') for l in f.read().splitlines()]

cycle = 0
x = 1
res = 0
for ins in instructions:
	match ins:
		case ["noop"]:
			cycle += 1
			res += get_cycle_value(cycle, x)
		case ["addx", num]:
			cycle += 2
			res += get_cycle_value(cycle - 1, x)
			res += get_cycle_value(cycle, x)
			x += int(num)
print(res)