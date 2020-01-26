from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import os

def sign_up():
	global nickname
	global email	
	global btt1
	nick = nickname.get()
	em = email.get()
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	c.execute('INSERT INTO acc(nickname, email) values(?, ?)', (nick, em))
	conn.commit()
	conn.close()
	nickname.delete(0, END)
	email.delete(0, END)
	btt1.delete(0, END)


loc = os.listdir()
if 'database.db' not in loc:
	conn = sqlite3.connect('database.db')
	c = conn.execute("""
		CREATE TABLE acc(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			nickname text,
			email text
	)""")
	conn.commit()
	conn.close()


root = Tk()
root.title('Databases')
root.geometry('500x500')

lbl1 = Label(root, text='You nickname:').grid(row=0, column=0)
nickname = Entry(root, width=10)
lbl2 = Label(root, text='You gmail.com:').grid(row=1, column=0)
email = Entry(root, width=10)
nickname.grid(row=0, column=1, pady=10, padx=50)
email.grid(row=1, column=1)

# btt1 = Button(root, text='SIGN up', command=sign_up).grid(row=3, column=0, pady=10, padx=50, ipadx=100)
btt1 = Button(root, text='SIGN up', command=sign_up)
btt1.grid(row=3, column=0, pady=10, padx=50)


root.mainloop()