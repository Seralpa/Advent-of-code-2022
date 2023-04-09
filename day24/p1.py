from __future__ import annotations
from dataclasses import dataclass
import os
import networkx as nx
import math


@dataclass(frozen=True)
class Blizzard:
	pos: tuple[int, int]
	direction: tuple[int, int]

	def move(self, max_y, max_x) -> Blizzard:
		newpos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
		if newpos[0] == 0:
			return Blizzard((max_y, self.pos[1]), self.direction)
		if newpos[0] > max_y:
			return Blizzard((1, self.pos[1]), self.direction)
		if newpos[1] == 0:
			return Blizzard((self.pos[0], max_x), self.direction)
		if newpos[1] > max_x:
			return Blizzard((self.pos[0], 1), self.direction)
		return Blizzard(newpos, self.direction)


def blizzard_cycles(blizzards: set[Blizzard], period: int, max_y: int, max_x: int) -> list[set[tuple[int, int]]]:
	cycles = []
	for _ in range(period):
		cycles.append({b.pos for b in blizzards})
		blizzards = set((b.move(max_y, max_x) for b in blizzards))
	return cycles


def create_graph(rows: int, cols: int, h_blizzards: set[Blizzard], v_blizzards: set[Blizzard]) -> nx.DiGraph:
	h_cycles = blizzard_cycles(h_blizzards, cols - 2, rows - 2, cols - 2)
	v_cycles = blizzard_cycles(v_blizzards, rows - 2, rows - 2, cols - 2)
	g = nx.DiGraph()
	lcm = math.lcm(rows - 2, cols - 2)
	for n in range(lcm):
		current_blizzards = h_cycles[n % len(h_cycles)] | v_cycles[n % len(v_cycles)]
		next_blizzards = h_cycles[(n + 1) % len(h_cycles)] | v_cycles[(n + 1) % len(v_cycles)]
		for i, r in enumerate(data):
			for j, c in enumerate(r):
				if c == "#" or (i, j) in current_blizzards:
					continue
				if (i, j) not in next_blizzards:
					g.add_edge((i, j, n), (i, j, (n + 1) % lcm))
				if i > 0 and (i - 1, j) not in next_blizzards:
					g.add_edge((i, j, n), (i - 1, j, (n + 1) % lcm))
				if i < rows - 1 and (i + 1, j) not in next_blizzards:
					g.add_edge((i, j, n), (i + 1, j, (n + 1) % lcm))
				if (i, j - 1) not in next_blizzards:
					g.add_edge((i, j, n), (i, j - 1, (n + 1) % lcm))
				if (i, j + 1) not in next_blizzards:
					g.add_edge((i, j, n), (i, j + 1, (n + 1) % lcm))
		g.add_edge((rows - 1, cols - 2, n), (rows - 1, cols - 2))
	return g


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [list(l) for l in f.read().splitlines()]

rows, cols = len(data), len(data[0])
dir_dict = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
h_blizzards: set[Blizzard] = set()
v_blizzards: set[Blizzard] = set()
for i, r in enumerate(data[1:-1], start=1):
	for j, c in enumerate(r[1:-1], start=1):
		if c in ("<", ">"):
			h_blizzards.add(Blizzard((i, j), dir_dict[c]))
		elif c in ("^", "v"):
			v_blizzards.add(Blizzard((i, j), dir_dict[c]))

g = create_graph(rows, cols, h_blizzards, v_blizzards)
print(nx.shortest_path_length(g, (0, 1, 0), (rows - 1, cols - 2)) - 1)