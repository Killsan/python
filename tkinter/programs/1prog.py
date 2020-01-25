from tkinter import *
from bs4 import BeautifulSoup as bs 
import requests

root = Tk()

input1 = Entry(root, width=20)
input1.pack()

def inp():
	url = input1.get()
	html_file = requests.get(url).text
	soup = bs(html_file, 'lxml')
	soup = soup.prettify()
	label1 = Label(root, text=soup).pack()

butt1= Button(root, command=inp, text='geturl').pack()

root.mainloop()