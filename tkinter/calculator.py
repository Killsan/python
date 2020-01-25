from tkinter import *
import os

def number():
	print('Fuck ya')

def clear():
	os.system('clear')

def calc():
	pass

root = Tk()
root.title('CALCULATOR')

input_place = Entry(root, width=27, borderwidth=2)
input_place.grid(row=0, column=0, columnspan=3)

butt1 = Button(root, text='1', padx=30, pady=30, command=number).grid(row=1, column=0)
butt2 = Button(root, text='2', padx=30, pady=30, command=number).grid(row=1, column=1)
butt3 = Button(root, text='3', padx=30, pady=30, command=number).grid(row=1, column=2)
butt4 = Button(root, text='4', padx=30, pady=30, command=number).grid(row=2, column=0)
butt5 = Button(root, text='5', padx=30, pady=30, command=number).grid(row=2, column=1)
butt6 = Button(root, text='6', padx=30, pady=30, command=number).grid(row=2, column=2)
butt7 = Button(root, text='7', padx=30, pady=30, command=number).grid(row=3, column=0)
butt8 = Button(root, text='8', padx=30, pady=30, command=number).grid(row=3, column=1)
butt9 = Button(root, text='9', padx=30, pady=30, command=number).grid(row=3, column=2)
butt0 = Button(root, text='0', padx=30, pady=30, command=number).grid(row=4, column=0)
butt_clear = Button(root, text='clear', padx=30, pady=30, command=clear).grid(row=4, column=1, columnspan=1	)
butt_equal = Button(root, text='=', padx=90, pady=30, command=calc).grid(row=5, column=0, columnspan=7)

root.mainloop()