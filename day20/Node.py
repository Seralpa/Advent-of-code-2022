from __future__ import annotations
from typing import Any


class Node:

	def __init__(self, data: Any = None, prev: Node = None, next: Node = None):
		self.data = data
		self.prev = prev
		self.next = next

	def insert_after(self, new: Node):
		new.prev = self
		new.next = self.next
		self.next.prev = new
		self.next = new

	def insert_before(self, new: Node):
		new.prev = self.prev
		new.next = self
		self.prev.next = new
		self.prev = new

	def pop(self):
		self.prev.next = self.next
		self.next.prev = self.prev
		self.next = None
		self.prev = None
		return self

	def pop_next(self) -> Node:
		return self.next.pop()

	def pop_prev(self) -> Node:
		return self.prev.pop()

	@staticmethod
	def from_list(l: list[Any], circular: bool = False) -> Node:
		""" Initialize linked list from a regular python list """
		prev = None
		head = None
		for i, e in enumerate(l):
			a = Node(e, prev=prev)
			if i == 0:
				head = a
			if i == len(l) - 1 and circular:
				a.next = head
				head.prev = a
			if prev:
				prev.next = a
			prev = a
		return head

	def __len__(self) -> int:
		""" Length of list ahead of self, if circular total length """
		cont = 0
		for _ in self:
			cont += 1
		return cont

	def __bool__(self) -> bool:
		return True

	def __iter__(self) -> NodeIterator:
		return NodeIterator(self)

	def __eq__(self, other: Node) -> bool:
		return self.data == other.data


class NodeIterator:

	def __init__(self, n: Node):
		self.current = n
		self.head = n
		self.times_iter_start = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.current:
			# keep track of how many times we iterated over head
			if self.current is self.head:
				self.times_iter_start += 1
			# if it's the second time passign over head stop
			if self.times_iter_start > 1:
				raise StopIteration

			curr = self.current
			self.current = self.current.next
			return curr
		else:
			raise StopIteration