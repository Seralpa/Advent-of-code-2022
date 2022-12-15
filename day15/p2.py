import os
from typing import Generator

MAX_SIZE = 4000000


class Sensor:
	pos: tuple[int, int]
	rang: int

	def __init__(self, sens: tuple[int, int], beacon: tuple[int, int]):
		self.pos = sens
		self.rang = abs(sens[0] - beacon[0]) + abs(sens[1] - beacon[1])

	def get_border(self) -> Generator[tuple[int, int], None, None]:
		x, y = self.pos[0] - self.rang - 1, self.pos[1]
		for _ in range(self.rang + 1):
			if x >= 0 and x <= MAX_SIZE and y >= 0 and y <= MAX_SIZE:
				yield x, y
			x += 1
			y += 1
		x, y = self.pos[0], self.pos[1] + self.rang + 1
		for _ in range(self.rang + 1):
			if x >= 0 and x <= MAX_SIZE and y >= 0 and y <= MAX_SIZE:
				yield x, y
			x += 1
			y -= 1
		x, y = self.pos[0] + self.rang + 1, self.pos[1]
		for _ in range(self.rang + 1):
			if x >= 0 and x <= MAX_SIZE and y >= 0 and y <= MAX_SIZE:
				yield x, y
			x -= 1
			y -= 1
		x, y = self.pos[0], self.pos[1] - self.rang - 1
		for _ in range(self.rang + 1):
			if x >= 0 and x <= MAX_SIZE and y >= 0 and y <= MAX_SIZE:
				yield x, y
			x -= 1
			y += 1

	def pos_in_range(self, pos: tuple[int, int]):
		return self.get_distance(pos) <= self.rang

	def get_distance(self, pos: tuple[int, int]) -> int:
		return abs(self.pos[0] - pos[0]) + abs(self.pos[1] - pos[1])


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	sensors = f.read().replace("Sensor at x=", "").replace(" closest beacon is at x=", "")
	sensors = [Sensor(*[tuple(map(int, t.split(", y="))) for t in l.split(":")]) for l in sensors.splitlines()]

for i, s in enumerate(sensors):
	print(f"border of sensor {i}/{len(sensors)}")
	for p in s.get_border():
		free = True
		for s1 in sensors:
			if s1.pos_in_range(p):
				free = False
				break
		if free:
			print(p[0] * 4000000 + p[1])
			exit()
