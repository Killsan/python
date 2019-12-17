def decorator(func):
	def wall ():
		print("---------------------------------------")
		func()
		print("---------------------------------------")
	return wall
@decorator
def Hello():
	print('Hello')
Hello()
