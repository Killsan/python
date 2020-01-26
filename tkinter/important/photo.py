from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('images.py')
# root.iconbitmap('path')

def forward(num):
	global lbl1
	global bt_foward
	global bt_back
	# lbl1.grid_forget()
	lbl1 = Label(root, image=images[num-1])
	lbl1.grid(row=0, column=0, columnspan=3)

def back():
	global lbl1
	global button_forward
	global button_back

img1 = ImageTk.PhotoImage(Image.open("imgs/umbrella.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("imgs/thns.png"))
img3 = ImageTk.PhotoImage(Image.open("imgs/vip.jpg"))

images = [img1, img2, img3]

lbl1 = Label(image=img1)
lbl1.grid(row=0, column=0, columnspan=3)

bt_back = Button(root, text='<<').grid(row=1, column=0)
bt2 = Button(root, text='Exit', command=root.quit).grid(row=1, column=1)
bt_foward = Button(root, text='>>', command=lambda: forward(0)).grid(row=1, column=2)

root.mainloop()