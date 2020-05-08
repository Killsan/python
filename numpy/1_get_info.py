import numpy as np 
import sys

a = np.array([1, 2, 4])
print('numpy array:')
print(a)

b = np.array([
	[9.0, 8.0, 7.0],
	[6.0, 5.0, 4.0]
])
print('\nsecond array:')
print(b)

print('\nget dimension <obj>.ndim:')
print(a.ndim)

print('\nget shape <obj>.shape')
print(a.shape)

print('\nget type <>.dtype')
print(a.dtype)

print('\nget syze <>.itemsize')
print(a.itemsize)

print('\nget total syze <>.nbytes')
print(a.nbytes)

print('-----------------------------------------------------------')

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print('\nnew array:')
print(a)

print('get elems: [1, 5]')
print(a[1, 5])

print('get elems: [1, -2]')
print(a[1, -2])

print('get elems: [1, 5]')
print(a[0, 5])


print('\nGet a specific row:')
print(a[0, :])

print('\nGet a specific column')
print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize]
print('-----------------------------------------------------------')
print(a)
print(a[0, 1:9:3])
#		^  ^ ^ ^oh, i wanned to see this moment 
#		^  ^ ^it was May 7 2020 when you started this shit
#       ^  ^numer of element to start with
#		^first array or the second one
print('-----------------------------------------------------------')