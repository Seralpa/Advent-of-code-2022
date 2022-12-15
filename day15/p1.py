import os


class Sensor:
	pos: tuple[int, int]
	rang: int

	def __init__(self, sens: tuple[int, int], beacon: tuple[int, int]):
		self.pos = sens
		self.rang = abs(sens[0] - beacon[0]) + abs(sens[1] - beacon[1])

	def get_distance(self, pos: tuple[int, int]) -> int:
		return abs(self.pos[0] - pos[0]) + abs(self.pos[1] - pos[1])

	def get_pos_in_range_y(self, y: int) -> set[tuple[int, int]]:
		dist = self.rang - self.get_distance((self.pos[0], y))
		return set([(x, y) for x in range(self.pos[0] - dist, self.pos[0] + dist)])


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	sensors = f.read().replace("Sensor at x=", "").replace(" closest beacon is at x=", "")
	sensors = [Sensor(*[tuple(map(int, t.split(", y="))) for t in l.split(":")]) for l in sensors.splitlines()]

covered_pos = set()
for s in sensors:
	covered_pos |= s.get_pos_in_range_y(2000000)
print(len(covered_pos))