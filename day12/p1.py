import os
import networkx as nx

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	area = [l for l in f.read().splitlines()]

G = nx.DiGraph()
start = ()
end = ()
for i, r in enumerate(area):
	for j, c in enumerate(r):
		if c == "S":
			start = (i, j)
			c = "a"
		if c == "E":
			end = (i, j)
			c = "z"

		if i > 0:
			if ord(area[i - 1][j]) - ord(c) <= 1:
				G.add_edge((i, j), (i - 1, j))
		if i + 1 < len(area):
			if ord(area[i + 1][j]) - ord(c) <= 1:
				G.add_edge((i, j), (i + 1, j))
		if j > 0:
			if ord(area[i][j - 1]) - ord(c) <= 1:
				G.add_edge((i, j), (i, j - 1))
		if j + 1 < len(r):
			if ord(area[i][j + 1]) - ord(c) <= 1:
				G.add_edge((i, j), (i, j + 1))

print(nx.shortest_path_length(G, start, end))