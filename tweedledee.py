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


def switch(brackets, i, j):
	tmp = brackets[i]
	brackets[i] = brackets[j]
	brackets[j] = tmp
	return brackets


brackets = get_word()
if len(brackets) % 4 != 0:
	print('impossible')
else:
	i = 0
	for i

