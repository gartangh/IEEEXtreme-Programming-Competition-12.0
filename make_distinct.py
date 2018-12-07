import math
from collections import defaultdict


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


n = get_number()
a = [get_number() for v in range(n)]
a.sort()

distinct = []
same = []
for i in a:
	if i not in distinct:
		distinct.append(i)
	else:
		same.append(i)

low = [-1] * n
high = [-1] * n

for i in same:
	for j in range(x, len(same)):
		k = 1
		while True:
			if i - k not in distinct:
				low[i] = k
				break

		k = 1
		while True:
			if i + k not in distinct:
				high[i] = k
				break



	x += 1
