from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames.py')

def ch_color():
	frm = LabelFrame(root, text='Frame1', padx=50, pady=50, bg='white')
	frm.grid(row=0, column=0)

frm = LabelFrame(root, text='Frame1', padx=50, pady=50, bg='blue', fg='white')
frm.grid(row=0, column=0)

bt1 = Button(frm, text='click', command=ch_color).grid(row=1, column=0)

root.mainloop()