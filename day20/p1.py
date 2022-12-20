import os
from Node import Node

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = Node.from_list([int(l) for l in f.read().splitlines()], circular=True)

node_list = [n for n in data]

for i, n in enumerate(node_list):
	d = n.next
	n.pop()
	if n.data > 0:
		for j in range(n.data % (len(node_list) - 1)):
			d = d.next
	elif n.data < 0:
		for j in range(abs(n.data) % (len(node_list) - 1)):
			d = d.prev
	d.insert_before(n)

for n in node_list:
	if n.data == 0:
		head = n

count = 0
for i in range(3000):
	head = head.next
	if (i + 1) % 1000 == 0:
		count += head.data
print(count)