import os
from dataclasses import dataclass


@dataclass
class Instruction:
	src: int
	dst: int
	num: int


def parse_instructions(ins_input: str) -> list[Instruction]:
	ins_input = ins_input.replace("move ", "").replace(" from ", ",").replace(" to ", ",")
	ins_input = [l.split(",") for l in ins_input.splitlines()]
	return [Instruction(int(src) - 1, int(dst) - 1, int(num)) for num, src, dst in ins_input]


def parse_startin_pos(start_input: str) -> list[list[str]]:
	stacks = list(zip(*start_input.splitlines()[:-1]))
	stacks = [reversed(stacks[i]) for i in range(1, len(stacks), 4)]
	for i, s in enumerate(stacks):
		stacks[i] = [c for c in s if c != " "]
	return stacks


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	start_input, ins_input = f.read().split('\n\n')

stacks = parse_startin_pos(start_input)
instructions = parse_instructions(ins_input)

for ins in instructions:
	stacks[ins.dst] += stacks[ins.src][-ins.num:]
	del stacks[ins.src][-ins.num:]

print("".join([s[-1] for s in stacks]))