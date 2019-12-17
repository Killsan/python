def numbers(a, b):
	if a > b:
		print(a + " > " + b)
	elif a < b:
		print(a + " < " + b)
	else:
		print("What the hell, dude")
num1 = input("WHat is the first? ")
num2 = input("WHat is the second? ")
numbers(num1, num2)