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
m = get_number()
s = get_number()

current = 0
time = 0
found = False
while n > 1:
	time += m*int(((n-1)/2) + 1) + s
	n /= 2

print(time)
