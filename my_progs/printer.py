def p(obj):
	try:
		if len(obj) <= 80:
			if len(obj) == 80:
				print('-' * len(obj))
				print(obj)
				print('-' * len(obj))
			else:
				print('-' * (len(obj)+1))
				print(obj)
				print('-' * (len(obj)+1))
		else:
			print(obj)
	except TypeError:
		print(obj)
