def Max_num():
	''' Print the bigest number '''
	num1 = input('1st number is ')
	num2 = input('2nd number is ')
	if num1 > num2:
		print(num1, ' is bigger')
	elif num1 < num2:
		print(num2, ' is bigger')
	else:
		print('=')
Max_num()
print(Max_num.__doc__)
