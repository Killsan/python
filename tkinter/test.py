from tkinter import *

root = Tk()

lbl1 = Label(root, text='How many 2 + 2? ').grid(row=0, column=0)

answer = IntVar()

Radiobutton(root, text='45', variable=answer, value=45, command=lambda: check(45)).grid(row=1, column=0, padx=10, pady=5)
Radiobutton(root, text='4', variable=answer, value=4, command=lambda: check(4)).grid(row=2, column=0, padx=10, pady=5)
Radiobutton(root, text='13', variable=answer, value=13, command=lambda: check(13)).grid(row=3, column=0, padx=10, pady=5)
Radiobutton(root, text='2', variable=answer, value=2, command=lambda: check(2)).grid(row=4, column=0, padx=10, pady=5)

def check(v):
	if v == 4:
		lbl2 = Label(root, text='COngrat').grid(row=5, column=0)
	else:
		lbl2 = Label(root, text='Stupid').grid(row=5, column=0)

ext = Button(root, command=root.quit, text='Exit').grid(row=6, column=0)

root.mainloop()