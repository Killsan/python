from tkinter import *

class Persons:
	def __init__(self, name, surname, nickname):
		self.name = name
		self.surname = surname,
		self.nickname = nickname

	def info(self):
		print('Name:', self.name)
		print("Surname:", self.surname)
		print("Nickname:", self.nickname)

def regish(name, surname, nickname):
	person = Persons(name, surname, nickname)
	print(person.name, person.nickname, person.surname)

def insert():
	name = Entry(root, width=10)
	name.grid(row=1, column=0)
	name = name.get()
	surname = Entry(root, width=10)
	surname.grid(row=2, column=0)
	surname = surname.get()
	nickname = Entry(root, width=10)
	nickname.grid(row=3, column=0)
	nickname = nickname.get()
	finish = Button(root, text="it's all", command=lambda: regish(name, surname, nickname)).grid(row=4, column=0)

root = Tk()
root.title('Second program')

reg = Button(root, text='regestration', command=insert, padx=30, pady=10).grid(row=0, column=0)
person = Entry(root, width=10)
get_info = Button(root, text='get info', command=lambda: Persons.info(person.get())).grid(row=2, column=0)

root.mainloop()