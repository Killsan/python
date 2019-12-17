def glob():
	x = 50
	print("X is: ", x)
	def non():
		nonlocal x
		x = input("Change x ")
	non()
	print('Now x is ', x)
glob()