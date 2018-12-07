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


for i in range(get_number()):
	needed_num = get_number()
	am = get_number()

	prov_num = [get_number() for v in range(am)]

	found = False
	out = '!OK'
	for second in range(1, am):
		for first in range(second):
			if needed_num == prov_num[first] + prov_num[second]:
				if prov_num[first] < prov_num[second]:
					out = str(prov_num[first]) + " " + str(prov_num[second])
				else:
					out = str(prov_num[second]) + " " + str(prov_num[first])
				found = True
				break
		if found:
			break
	print(out)
