from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox

root = Tk()

def click():
	messagebox.showinfo("Message", 'Go in hell')
	#messagebox.showwarning(<text>, <text>)
	#messagebox.showerror()
	#messagebox.askquestion()
	#messagebox.asokcancel()
	#messagebox.askyesno()

def question():
	response = messagebox.askyesno('', 'Are you an asshole? ')
	print(response)

bt1 = Button(root, text='click', command=click).pack()
bt2 = Button(root, text='Serious question', command=question).pack()


root.mainloop()