import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])


a[1,5] = 20
print(a)

print('')

a[:, 2] = [1, 2]
print(a)


print('------------------------3d shit-----------------------')

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# Get specific element (work outside in)

print(b[0,1,0])