from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class File:
	name: str
	size: int


@dataclass
class Dir:
	name: str
	parent: Dir
	files: list[File] = field(default_factory=lambda: list())
	dirs: list[Dir] = field(default_factory=lambda: list())
	# for caching
	size: int = -1

	def get_size(self) -> int:
		if self.size != -1:
			return self.size

		self.size = sum([f.size for f in self.files])
		self.size += sum([d.get_size() for d in self.dirs])
		return self.size

	def get_dir_by_name(self, name: str) -> Dir:
		for d in self.dirs:
			if d.name == name:
				return d

	def append_elegible_subdirs(self, elegible: list[Dir], criteria: Callable[[Dir], bool]):
		if criteria(self):
			elegible.append(self)
		for d in self.dirs:
			d.append_elegible_subdirs(elegible, criteria)