a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
	if i < 5:
		# print(i)
		pass
	else:
		continue

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in b:
	if i in a:
		c.append(i)
# print(a)
# print(b)
# print(c)

a = [21, 4, 2, 12, 3, 76, 54, 7, 35, 86, 24]
# print(a)

a.sort(reverse=True)
# print(a)

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
# print(dict_a, dict_b, dict_c)

result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
# print(result)

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

# num = int(input('Enter the random number: '))
# print(type(num))
# num = str(num)
# print(type(num))

# print(int('ABC', 15))

def pascal_triangle(n):
   row = [1]
   y = [0]
   for x in range(max(n, 0)):
      print(row)
      row = [left + right for left, right in zip(row + y, y + row)]
   
# pascal_triangle(6) 

# string = input('Enter something: ')
# print(string)

# string = ''.join(reversed(string))
# print(string)

def palindrom(string):
	if string == ''.join(reversed(string)):
		print('Yes, it is')
	else:
		print('no')

# string = input('Enter your word: ')
# palindrom(string)

