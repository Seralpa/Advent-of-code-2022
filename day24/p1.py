from __future__ import annotations
from dataclasses import dataclass
import os
import networkx as nx


@dataclass(frozen=True)
class Blizzard:
	pos: tuple[int, int]
	direction: tuple[int, int]

	def move(self, max_y, max_x) -> Blizzard:
		newpos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
		if newpos[0] == 0:
			return Blizzard((max_y - 1, self.pos[1]), self.direction)
		if newpos[0] == max_y:
			return Blizzard((1, self.pos[1]), self.direction)
		if newpos[1] == 0:
			return Blizzard((self.pos[0], max_x - 1), self.direction)
		if newpos[1] == max_x:
			return Blizzard((self.pos[0], 1), self.direction)
		return Blizzard(newpos, self.direction)


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [list(l) for l in f.read().splitlines()]

dir_dict = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
blizzards: set[Blizzard] = set()
for i, r in enumerate(data[1:-1], start=1):
	for j, c in enumerate(r[1:-1], start=1):
		if c in dir_dict.keys():
			blizzards.add(Blizzard((i, j), dir_dict[c]))

g = nx.DiGraph()
start = (0, 1)
end = (len(data) - 1, len(data[0]) - 2)
for n in range(100000):
	next_blizzards = set((b.move(len(data) - 1, len(data[0]) - 1) for b in blizzards))
	next_blizzards_pos = set((b.move(len(data) - 1, len(data[0]) - 1).pos for b in blizzards))
	for i, r in enumerate(data):
		for j, c in enumerate(r):
			if c == "#":
				continue
			if (i, j) not in next_blizzards_pos:
				g.add_edge((i, j, n), (i, j, n + 1))
			if i > 0 and (i - 1, j) not in next_blizzards_pos:
				g.add_edge((i, j, n), (i - 1, j, n + 1))
			if i < len(data) - 1 and (i + 1, j) not in next_blizzards_pos:
				g.add_edge((i, j, n), (i + 1, j, n + 1))
			if (i, j - 1) not in next_blizzards_pos:
				g.add_edge((i, j, n), (i, j - 1, n + 1))
			if (i, j + 1) not in next_blizzards_pos:
				g.add_edge((i, j, n), (i, j + 1, n + 1))
	blizzards = next_blizzards
	if nx.has_path(g, start + (0,), end + (n,)):
		print(n)
		break