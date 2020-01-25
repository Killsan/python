from tkinter import *

def def1():
	label1 = Label(root, text=message.get()).pack()

root = Tk()

message = StringVar()
input1 = Entry(root, width=10, textvariable=message).pack()
butt1 = Button(root, width=10, command=def1).pack()

root.mainloop()