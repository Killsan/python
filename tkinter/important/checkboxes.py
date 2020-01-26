from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.geometry('500x500')

var = IntVar()

chkbox = Checkbutton(root, text='click', variable=var, onvalue='on', offvalue='off').pack()
chkbox.deselect()
# lbl1 = Label(root, text=var.get()).pack()

def update():
	lbl1 = Label(root, text=var.get()).pack()

btt1 = Button(root, text='click', command=update).pack()


root.mainloop()