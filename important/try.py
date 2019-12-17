while True:
	try:
		a = int(input("Enter the first number "))
		b = int(input("Enter the second number "))
	except ValueError:
		print("Only numbers")
		continue
	else:
		print(a + b)
		break
	#finally:
		#print("You'd got your answer")
