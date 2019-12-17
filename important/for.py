for i in range(1, 5):
    print(i)
print('')
print('==========================')
print('')
for g in 'Hello':
	print(g * 2, end="")
print('')
print("==============================")
print('')
spi = ['apple', 'shotgun', 'phone']
for it in spi:
	print(it + " ", end='')
	if it == 'shothun':
		print("I found shotgun")
		break
else:
	print("Here is no shotguns")
