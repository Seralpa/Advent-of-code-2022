import os
from typing import Generator

MAX_SIZE = 4000000
Point = tuple[int, int]


class Sensor:
	x: int
	y: int
	range_: int

	def __init__(self, pos: Point, beacon: Point):
		self.x = pos[0]
		self.y = pos[1]
		self.range_ = abs(pos[0] - beacon[0]) + abs(pos[1] - beacon[1])

	def get_border_ranges(self) -> list[tuple[Point, Point]]:
		n = self.x - self.range_ - 1, self.y
		s = self.x + self.range_ + 1, self.y
		w = self.x, self.y - self.range_ - 1
		e = self.x, self.y + self.range_ + 1
		return [(n, w), (n, e), (w, s), (e, s)]

	def remove_range_overlap(self, r: tuple[Point, Point]) -> tuple[Point, Point]:
		# NOTE the case when the scanner overlaps only the middle of the range is not handled
		# as in the end all ranges will be reduced to a single point
		p1_in_range = self.pos_in_range(r[0])
		p2_in_range = self.pos_in_range(r[1])
		if p1_in_range and p2_in_range:
			return (0, 0), (0, 0)
		# dir_x will always be 1 because of how the ranges are constructed initially
		dir_y = 1 if r[1][1] >= r[0][1] else -1
		if p1_in_range:
			d_x, d_y = self.get_distance_xy(r[0])
			d = d_x + d_y * dir_y
			delta = ((self.range_ - d) // 2) + 1
			return (r[0][0] + delta, r[0][1] + delta * dir_y), r[1]
		elif p2_in_range:
			d_x, d_y = self.get_distance_xy(r[1])
			d = -d_x - d_y * dir_y
			delta = (self.range_ - d + 1) // 2
			return r[0], (r[1][0] - delta, r[1][1] - delta * dir_y)
		else:
			return r

	def pos_in_range(self, pos: Point):
		return self.get_distance(pos) <= self.range_

	def get_distance(self, pos: Point) -> int:
		return abs(self.x - pos[0]) + abs(self.y - pos[1])

	def get_distance_xy(self, pos: Point) -> tuple[int, int]:
		return pos[0] - self.x, pos[1] - self.y


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	sensors = f.read().replace("Sensor at x=", "").replace(" closest beacon is at x=", "")
	sensors = [Sensor(*[tuple(map(int, t.split(", y="))) for t in l.split(":")]) for l in sensors.splitlines()]

ranges = []
for s in sensors:
	ranges += s.get_border_ranges()

for i in range(len(ranges)):
	if ranges[i][0][0] > MAX_SIZE or ranges[i][1][0] < 0:
		ranges[i] = ((0, 0), (0, 0))
		continue
	dir_y = 1 if ranges[i][1][1] >= ranges[i][0][1] else -1
	if ranges[i][0][0] < 0:
		ranges[i] = (0, ranges[i][0][1] - ranges[i][0][0] * dir_y), ranges[i][1]
	if ranges[i][1][0] > MAX_SIZE:
		ranges[i] = ranges[i][0], (MAX_SIZE, ranges[i][1][1] - (ranges[i][1][0] - MAX_SIZE) * dir_y)

	if dir_y == 1:
		if ranges[i][1][1] < 0 or ranges[i][0][1] > MAX_SIZE:
			ranges[i] = ((0, 0), (0, 0))
			continue
		if ranges[i][0][1] < 0:
			ranges[i] = (ranges[i][0][0] - ranges[i][0][1], 0), ranges[i][1]
		if ranges[i][1][1] > MAX_SIZE:
			ranges[i] = ranges[i][0], (ranges[i][1][0] - (ranges[i][1][1] - MAX_SIZE), MAX_SIZE)
	else:
		if ranges[i][0][1] < 0 or ranges[i][1][1] > MAX_SIZE:
			ranges[i] = ((0, 0), (0, 0))
			continue
		if ranges[i][1][1] < 0:
			ranges[i] = ranges[i][0], (ranges[i][1][0] + ranges[i][1][1], 0)
		if ranges[i][0][1] > MAX_SIZE:
			ranges[i] = (ranges[i][0][0] + (ranges[i][0][1] - MAX_SIZE), MAX_SIZE), ranges[i][1]

while len(ranges) > 1 or ranges[0][0] != ranges[0][1]:
	for s in sensors:
		for i, r in enumerate(ranges):
			ranges[i] = s.remove_range_overlap(r)
	ranges = list(set([r for r in ranges if r != ((0, 0), (0, 0))]))

print(ranges[0][0][0] * 4000000 + ranges[0][0][1])
