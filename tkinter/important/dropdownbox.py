from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.geometry('500x500')

def show(var):
	print(clicked.get())

clicked = StringVar()
clicked.set('Select')

drp_box = OptionMenu(root, clicked, 'monday', 'thusday', 'wednsday', 'thursday', command=show).pack()


root.mainloop()