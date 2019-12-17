file1 = open('test0.txt')
# r - open for reading
# w - открытие на запись, содержимое удаляется, eсли файла не сущ, созд новый
# x - открыть на запись, если файла не сущ, иначе исключение
# a - you can add info in the end of the text
# b - открытие в двоичном режиме
# t - oткрытие в текстовом режиме
# + - открытие на чтение и запись
print(file1.read(3))
for i in file1:
	print(i)
file1.close()
#creating a new file
file2 = open('test1.txt', 'w')
file2.write('Hello, i wanna pray')
file2 = open('test1.txt')
for j in file2:
	print(j)
file2.close()