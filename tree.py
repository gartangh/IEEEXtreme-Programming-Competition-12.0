# a simple parser for python. use get_number() and get_word() to read
def parser():
	while 1:
		data = list(input().split(' '))
		for number in data:
			if len(number) > 0:
				yield (number)


input_parser = parser()


def get_word():
	global input_parser
	return next(input_parser)


def get_number():
	data = get_word()
	try:
		return int(data)
	except ValueError:
		return float(data)


# numpy and scipy are available for use
import numpy
import scipy


class Node:
	def __init__(self, ch=None):
		self.left = None
		self.right = None
		self.ch = ch
		self.str_in = None
		self.str_pre = None


while True:
	infix = get_word()
	prefix = get_word()
	if infix == '' or prefix == '':
		break
	Top = Node()

	Top.str_in = infix
	to_process = [Top]

	current_nodes = [Top]
	for c in prefix:
		for t in current_nodes:
			if c in t.str_in:
				handle_node = t

		spl = handle_node.str_in.split(c)
		left = spl[0]
		right = spl[1]

		handle_node.ch = c
		current_nodes.remove(handle_node)

		if left != "":
			new_l = Node()
			handle_node.left = new_l
			handle_node.left.str_in = left
			current_nodes.append(new_l)

		if right != "":
			new_r = Node()
			handle_node.right = new_r
			handle_node.right.str_in = right
			current_nodes.append(new_r)

	layers = [[Top]]
	current_index = 0
	cont = True
	while cont:
		cont = False
		for el in layers[current_index]:

			if el is not None:
				cont = True

		if cont:
			new_l = []
			for el in layers[current_index]:
				if el is None:
					new_l.append(None)
					new_l.append(None)
				else:
					new_l.append(el.left)
					new_l.append(el.right)
			current_index += 1
			layers.append(new_l)

	print_layer = [""] * (current_index)
	for i in range(current_index):
		print_layer[i] = print_layer[i] + " " * ((current_index - i - 1) * 2 - 1)
		for el in layers[i]:
			if el is not None:
				print_layer[i] = print_layer[i] + el.ch
			else:
				print_layer[i] = print_layer[i] + ' '
			print_layer[i] = print_layer[i] + " " * ((current_index - i) * 2 - 1)

	for s in print_layer:
		print(s)
