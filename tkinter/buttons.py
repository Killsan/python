from tkinter import *

def rand():
	for i in range(50):
		label = Label(root, text="it's a button")
		label.grid(row=1, column=2)

root = Tk()

butt1 = Button(root, text='PUsh', state=DISABLED) 
butt1.grid(row=1, column=1)

#=============================================================================
butt2 = Button(root, text='cmon', padx=100, pady=30, fg='black', bg='red')
butt2.grid(row=2, column=1)
#fg='font color', bg='background color' padx=lenght, pady=hieght
#=============================================================================

butt3 = Button(root, text='click', padx=100, pady=10, command=rand)
butt3.grid(row=3, column=5)
#command=function

root.mainloop()