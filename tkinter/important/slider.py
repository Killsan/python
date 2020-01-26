from tkinter import *
from PIL import ImageTk, Image 


root = Tk()
root.geometry('500x500')

vertical = Scale(root, from_=0, to=200).pack()

def slide(var):
	print(horizontal.get())

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=slide)
horizontal.pack()


bt1 = Button(root, text='click', command=slide).pack()

root.mainloop()