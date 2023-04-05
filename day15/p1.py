import os

Point = tuple[int, int]


class Sensor:
	x: int
	y: int
	range_: int

	def __init__(self, pos: Point, beacon: Point):
		self.x = pos[0]
		self.y = pos[1]
		self.range_ = abs(pos[0] - beacon[0]) + abs(pos[1] - beacon[1])

	def get_distance(self, pos: Point) -> int:
		return abs(self.x - pos[0]) + abs(self.y - pos[1])

	def get_covered_range_in_y(self, y: int) -> Point:
		dist = self.range_ - self.get_distance((self.x, y))
		return (self.x - dist, self.x + dist) if dist >= 0 else (0, 0)


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	sensors = f.read().replace("Sensor at x=", "").replace(" closest beacon is at x=", "")
	sensors = [Sensor(*[tuple(map(int, t.split(", y="))) for t in l.split(":")]) for l in sensors.splitlines()]

ranges = sorted([s.get_covered_range_in_y(2000000) for s in sensors])
for i in range(len(ranges) - 1):
	r1, r2 = ranges[i], ranges[i + 1]
	if max(r1[0], r2[0]) <= min(r1[1], r2[1]):
		ranges[i] = (0, 0)
		ranges[i + 1] = (min(r1[0], r2[0]), max(r1[1], r2[1]))

print(sum(r[1] - r[0] for r in ranges))