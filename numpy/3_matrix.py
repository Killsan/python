import numpy as np 

print(np.zeros((2,3,3)))

print(np.ones((4,2,2)))


print(np.full((4,3), 99))
#			 ^ ^   ^values
#			 ^ ^x lenght
#			 ^y lenght	

#a = np.full_like(<array>, <value>)

#Random decimal numbers

print(np.random.rand(4,2,3))

print(np.random.randint(-4,7, size=(3,3)))

print(np.identity(5))

arr = np.array([1,2,3])

print(np.repeat(arr, 3))