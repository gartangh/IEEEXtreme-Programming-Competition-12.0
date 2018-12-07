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
import scipy.spatial.distance
import sys


def send(char, guess):
	guess_str = ''
	for i in guess:
		guess_str += ' ' + str(i)
	print(char + guess_str)
	sys.stdout.flush()
	if char == 'Q':
		return get_number()
	else:
		return None


def inver(guess):
	for k in range(len(guess)):
		guess[k] = 1-guess[k]

for i in range(get_number()):
	n = get_number()
	if n == 1:
		score = send('Q', [0])
		if score == 1:
			send('A', [0])
			break
		else:
			send('A', [1])
			break

	# create all possible solutions
	possible_solutions = [[0], [1]]
	for j in range(2, n + 1):
		# make a copy
		for k in range(len(possible_solutions)):
			possible_solutions_copy = []
			for l in range(len(possible_solutions[k])):
				if possible_solutions[k][l] == 0:
					possible_solutions_copy.append(0)
				else:
					possible_solutions_copy.append(1)
			possible_solutions.append(possible_solutions_copy)
		# append 0's and 1's
		for k in range(pow(2, j)):
			if k < pow(2, j - 1):
				possible_solutions[k].append(0)
			else:
				possible_solutions[k].append(1)

	# start guessing
	for j in range(n + 1):
		guess = possible_solutions[0]
		distance = n - send('Q', guess)
		del possible_solutions[0]

		# correct guess
		if distance == 0:
			send('A', guess)
			break

		# opposite guess
		if distance == n:
			guess = invert(guess)
			send('A', guess)
			break

		# remove all impossible solutions
		to_remove = []
		for k in range(len(possible_solutions)):
			hamming = scipy.spatial.distance.hamming(guess, possible_solutions[k])*n
			if hamming != distance:
				to_remove.append(k)
		for k in sorted(to_remove, reverse=True):
			del possible_solutions[k]

		# found answer
		if len(possible_solutions) == 1:
			guess = possible_solutions[0]
			send('A', guess)
			break
