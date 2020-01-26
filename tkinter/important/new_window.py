from tkinter import *
from PIL import ImageTk, Image 

root = Tk()

def new():
	global top
	top = Toplevel()
	lbl_tp = Label(top, text='Hell with you').grid(row=0, column=0, padx=20)
	bt_ex = Button(top, text='Exit', command=top.quit).grid(row=1, column=0)

bt1 = Button(root, text='click', command=new).grid(row=0, column=0)

root.mainloop()