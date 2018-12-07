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

n = get_number()
q = get_number()


class Div:
	divs = []

	def __init__(self, name, parent, size1, size2):
		self.name = name
		self.parent = parent
		self.size1 = size1
		self.size2 = size2
		self.lower1 = 0
		self.upper1 = 0
		self.lower2 = 0
		self.upper2 = 0

		if size1 > 0:
			self.lower1 = size1
			self.uper1 = size1
		if size2 > 0:
			self.lower1 = size2
			self.uper2 = size2

		Div.divs.append(self)

	def get_parent(self):
		if self.parent == 'NONE':
			return None

		for i in Div.divs:
			if i.name == self.parent:
				return i

	def get_children(self):
		children = []
		for i in Div.divs:
			if i.parent == self.name:
				children.append(i)
		return children

	def get_brothers(self):
		if not self.get_parent():
			return []

		children = self.get_parent().get_children()
		for i in children:
			if i.name == self.name:
				del children[children.index(i)]
				break

		return children

	def lower1(self):
		if self.size1 != 0:
			return self.size1

		return self.down()

	def upper1(self):
		if self.size1 != 0:
			return self.size1

		upper1 = self.upper2()
		for i in self.get_children():
			upper1 -= i.lower2()

		return upper1

	def lower2(self):
		if self.size2 != 0:
			return size2

		a = self.down()

		if not self.get_parent():
			return a

		b = 0
		if self.get_parent():
			size_children = 0
			for i in self.get_brothers():
				size_children += i.down()

			b = self.get_parent().down() - size_children
		# wrong
		return max(a, b) + 1

	def upper2(self):
		if self.size2 != 0:
			return self.size2

		a = self.down()

		if not self.get_parent():
			return a

		# wrong
		b = self.get_parent().size2 if self.get_parent().size2 > 0 else self.get_parent().size1
		b -= self.get_parent().size1 if self.get_parent().size1 > 0 else 1
		for i in self.get_brothers():
			b -= i.down()

		return max(a, b)

	def down(self):
		"""amount of people certain"""
		a = self.size1 if self.size1 > 0 else 1
		for i in self.get_children():
			a += i.size2 if i.size2 > 0 else i.down()

		return a

	@staticmethod
	def get_div(name):
		for i in Div.divs:
			if i.name == name:
				return i

	@staticmethod
	def get_root():
		for i in Div.divs:
			if i.parent == 'NONE':
				return i

		return None

	@staticmethod
	def solve():
		root = Div.get_root()

		if root:
			if root.size1 > 0 and root.size2 > 0:
				to_distribute = root.size2 - root.size1


for i in range(n):
	name = get_word()
	parent = get_word()
	size1 = get_number()
	size2 = get_number()

	Div(name, parent, size1, size2)

Div.solve()

for i in range(q):
	div = Div.get_div(get_word())

	if get_number() == 1:
		print(f'{div.lower1} {div.upper1}')
	else:
		print(f'{div.lower2} {div.upper2}')
