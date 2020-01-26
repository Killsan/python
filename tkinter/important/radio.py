from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title('Radio.py')

r = IntVar()
r.set('2')

def click(v):
	lbl1 = Label(root, text=v).grid(row=2, column=0)


Radiobutton(root, text='First option', variable=r, value=1, command=lambda: click(r.get())).grid(row=0, column=0)
Radiobutton(root, text='Second option', variable=r, value=2, command=lambda: click(r.get())).grid(row=1, column=0)

lbl1 = Label(root, text=r.get())
lbl1.grid(row=2, column=0)

root.mainloop()