import math
import os, re

bp_re = re.compile(r"Each (\w+) robot costs (\d+) (\w+)(?: and (\d+) (\w+))?")

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
str_to_i = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}


def get_num_geodes(bp: dict[str, dict[str, int]], res: tuple[int, ...], robots: tuple[int, ...], time: int) -> int:
	if time == 1:
		return res[GEODE] + robots[GEODE]

	# check if state seen
	scores = []
	for bot in reversed(bp.keys()):
		if bot != "geode" and robots[str_to_i[bot]] >= max_bots[str_to_i[bot]]:
			continue

		# calculate time to build bot
		time_bot = 0
		can_build = True
		for r, v in bp[bot].items():
			if robots[str_to_i[r]] == 0:
				can_build = False
				break
			time_bot = max(max(math.ceil((v - res[str_to_i[r]]) / robots[str_to_i[r]]), 0), time_bot)
		time_bot += 1
		if time - time_bot <= 0 or not can_build:
			continue
		# update res according to time and bot
		tmp_res = [res[r] + robots[r] * time_bot for r in str_to_i.values()]
		for r, v in bp[bot].items():
			tmp_res[str_to_i[r]] -= v
		tmp_res = tuple(tmp_res)
		# update bots
		tmp_bots = list(robots)
		tmp_bots[str_to_i[bot]] += 1
		tmp_bots = tuple(tmp_bots)
		# call recursive
		scores.append(get_num_geodes(bp, tmp_res, tmp_bots, time - time_bot))

	if not scores:
		return res[GEODE] + time * robots[GEODE]
	return max(scores)


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l.split(": ")[1].split(". ") for l in f.read().splitlines()]

blueprints: list[dict[str, dict[str, int]]] = []
for b in data:
	robots: dict[str, dict[str, int]] = {}
	for robot in b:
		if not (bot_match := bp_re.match(robot)):
			print(f"err regex not match: {robot}")
			continue
		a = bot_match.groups()
		res = a[0]
		cost = dict()
		for i in range(1, len(a), 2):
			if not a[i]:
				break
			cost[a[i + 1]] = int(a[i])
		robots[res] = cost
	blueprints.append(robots)

result = 0
for i, bp in enumerate(blueprints, start=1):
	max_bots = [0, 0, 0]
	for res in ["ore", "clay", "obsidian"]:
		for cost in bp.values():
			max_bots[str_to_i[res]] = max(max_bots[str_to_i[res]], cost.get(res, 0))
	quality = i * get_num_geodes(bp, (0, 0, 0, 0), (1, 0, 0, 0), 24)
	result += quality
print(result)
