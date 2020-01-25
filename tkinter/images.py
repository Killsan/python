from tkinter import *
from PIL import Image, ImageTk
# from PIL import ImageTk, Image
import os

root = Tk()
root.title('Image')
# root.iconbitmap((os.path.dirname(os.path.abspath(__file__))+"/icon.ico")) 

img1 = PhotoImage(file = 'imgs/github.png')
img1 = img1.resize((250, 250), Image.ANTIALIAS)
label1 = Label(image=img1).pack()

b_exit = Button(root, text='Exit', command=root.quit).pack()
root.mainloop()