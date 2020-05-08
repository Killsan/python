import numpy as np 

# arr = np.array([
# 	[1,1,1,1,1],
# 	[1,0,0,0,1],
# 	[1,0,9,0,1],
# 	[1,0,0,0,1],
# 	[1,1,1,1,1]
# ])
# print(arr)

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z 
print(output)