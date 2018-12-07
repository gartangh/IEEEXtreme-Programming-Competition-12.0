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
import sys

t = get_number()
for i in range(t):
	n = get_number()
	guess = [0] * n
	prev_score = None
	score = None


	def create_guess(i):
		global guess, prev_score, score, n
		if i < n:
			invert_i(i)
		if score < prev_score:
			invert_i(i - 1)


	def create_str(char):
		global guess
		guess_str = ''
		for i in guess:
			guess_str += ' ' + str(i)
		print(char + guess_str)
		sys.stdout.flush()
		if char == 'Q':
			return int(input())


	def invert_i(i):
		global guess
		guess[i] = 1 - guess[i]


	prev_score = create_str('Q')

	if n == 1 and prev_score == 1:
		create_str('A')
		continue
	elif n == 1:
		invert_i(0)
		create_str('A')
		continue

	if n == prev_score:
		create_str('A')
		continue

	first_score = prev_score
	invert_i(0)
	score = create_str('Q')

	if n == score:
		create_str('A')
		continue

	for i in range(1, n):
		if i != n - 1:
			invert_i(i)
		if score <= prev_score:
			invert_i(i - 1)
		prev_score = score

		if i != n - 1:
			score = create_str('Q')
			if score == n:
				create_str('A')
				break
		else:
			tot = 0
			for val in guess:
				tot += val

			if n - first_score != tot:
				invert_i(n - 1)
			create_str('A')
			break
