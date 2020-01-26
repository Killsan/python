from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog

root = Tk()

def choose():
	global lbl1
	global img1
	root.filename = filedialog.askopenfilename(initialdir='images/', title='Select the file', filetypes=(('png files', '*.png'), ('all files', '*.*')))
	img1 = ImageTk.PhotoImage(Image.open(root.filename))
	lbl1 = Label(root, image=img1).grid(row=3, column=0, pady=5, padx=10)

bt = Button(root, text='chose file', command=choose).grid(row=0, column=0, pady=10, padx=15)

root.mainloop()