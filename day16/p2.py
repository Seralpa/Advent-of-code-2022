from dataclasses import dataclass
import networkx as nx
import os
from itertools import chain, combinations


def powerset(iterable):
	"powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


@dataclass
class Valve:
	name: str
	flow: int
	tunnels: list[str]


def dfs(node: str, time: int, pressure: int, open_valves: frozenset[str], n_nodes: int, smallG: nx.DiGraph):
	if time <= 0:
		return pressure

	if (node, open_valves) in seen:
		if seen[(node, open_valves)][0] >= pressure and seen[(node, open_valves)][1] >= time:
			return seen[(node, open_valves)][0]

	seen[(node, open_valves)] = (pressure, time)

	if len(open_valves) == n_nodes:
		return pressure

	scores = []
	if node not in open_valves and valves[node].flow > 0:
		scores.append(dfs(node, time - 1, pressure + valves[node].flow * (time - 1), open_valves | {node}, n_nodes, smallG))
	for neigh in smallG.neighbors(node):
		if neigh not in open_valves:
			new_time = time - smallG[node][neigh]["weight"] - 1
			if new_time >= 0:
				scores.append(
				    dfs(neigh, new_time, pressure + valves[neigh].flow * new_time, open_valves | {neigh}, n_nodes, smallG))
	if not scores:
		return pressure
	return max(scores)


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read().replace("Valve ", "").replace(" has flow rate=", ";").replace(" tunnels lead to valves ", "")
	data = data.replace(" tunnel leads to valve ", "")
	data = [l.split(";") for l in data.splitlines()]

valves: dict[str, Valve] = dict()

for v, flow, tun in data:
	valves[v] = Valve(v, int(flow), tun.split(", "))

fullG = nx.Graph()
for v in valves.values():
	fullG.add_edges_from([(v.name, v2) for v2 in v.tunnels])

working_valves = {v.name for v in valves.values() if v.flow > 0}

subsets = set(map(frozenset, powerset(working_valves)))
sub_solves: dict[frozenset, int] = dict()
for i, s in enumerate(subsets):
	if i % 1000 == 0:
		print(f"solving subset {i}/{len(subsets)}")
	smallG = nx.DiGraph()
	for v1, v2 in combinations(s, 2):
		l = nx.shortest_path_length(fullG, v1, v2)
		smallG.add_edge(v1, v2, weight=l)
		smallG.add_edge(v2, v1, weight=l)

	for v in s:
		l = nx.shortest_path_length(fullG, "AA", v)
		smallG.add_edge("AA", v, weight=l)

	seen: dict[tuple, tuple] = {}
	sub_solves[s] = dfs("AA", 26, 0, frozenset(), len(s), smallG)

print(max([v + sub_solves[frozenset(working_valves - k)] for k, v in sub_solves.items()]))