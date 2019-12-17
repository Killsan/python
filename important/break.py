while True:
	word = input('Enter the command ')
	if word == 'stop' or word=='break' or word=='exit':
		break
	elif word == 'help':
		print('Here is commands: 1. break 2. stop 3. exit')
	else:
		print("It will never stop, write 'help' to see another commands that is connected")
		