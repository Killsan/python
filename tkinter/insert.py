from tkinter import *

root = Tk()

inp = Entry(root)
inp.pack()

def insrt():
	inp.insert(0, 'hello')

b1 = Button(root, command=insrt, text='click').pack()

root.mainloop()