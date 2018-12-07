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


class Star:
	def __init__(self, start, finish, desire):
		self.start = start
		self.finish = finish
		self.profit = desire


def binary_search(job, start_index):
	lo = 0
	hi = start_index - 1

	while lo <= hi:
		mid = (lo + hi) // 2
		if job[mid].finish <= job[start_index].start:
			if job[mid + 1].finish < job[start_index].start:
				lo = mid + 1
			else:
				return mid
		else:
			hi = mid - 1
	return -1


def schedule(job):
	job = sorted(job, key=lambda j: j.finish)

	length = len(job)
	table = [0 for _ in range(length)]
	table[0] = job[0].profit

	for i in range(1, length):
		incl_prof = job[i].profit
		prof_from_search = binary_search(job, i)
		if prof_from_search != -1:
			incl_prof += table[prof_from_search]

		table[i] = max(incl_prof, table[i - 1])

	return table[length - 1]


n = get_number()
stars = [Star(get_number(), get_number(), get_number()) for v in range(n)]
print(schedule(stars))
