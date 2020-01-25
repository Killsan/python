from tkinter import *

def def1(v):
	msg = input1.get()
	input1.delete(0, END)
	input1.insert(0, str(msg) + str(v))

def clear():
	input1.delete(0, END)

root = Tk()
root.title('2INput.py')

input1 = Entry(root)
input1.pack()

butt1 = Button(root, text='0', command=lambda: def1(0)).pack()
butt2 = Button(root, text='1', command=lambda: def1(1)).pack()
butt3 = Button(root, text='clear', command=clear).pack()

root.mainloop()