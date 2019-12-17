import os
print(os.getlogin()) #user on unix system
print('-------------------------------------------')
print(os.getpid()) #the id of this process
print('-------------------------------------------')
print(os.uname()) #os info
print('-------------------------------------------')
print(os.getcwd())
print('-------------------------------------------')
print(os.listdir('/home/killsan/it doesnt metter/python')) #print's all files in the folder
print('-------------------------------------------')
print(os.name)
print('-------------------------------------------')
# print(os.chdir('important') #you can change the directory 
#os.system(<command>) #system will do your command