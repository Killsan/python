import socket
import os
import requests
import sqlite3 as db
from bs4 import BeautifulSoup as bs

os.system('clear')
#=================================SOCKET===================================


def clear():
	loc = os.getcwd()
	if 'C:' in loc or 'D:' in loc:
		os.system('cls')
	else:
		os.system('clear')

def identify(addr):
	nick = client.recv(1024)
	nick = nick.decode('utf-8')
	clients = []
	clients.append(nick)

def tcp_recv(client):
	msg = client.recv(1024)
	url = msg.decode('utf-8')
	try:
		html_file = requests.get(url).text
	except requests.exceptions.InvalidURL:
		client.send(bytes('Invalid URL', 'utf-8'))
	except requests.exceptions.MissingSchema:
		client.send(bytes('Invalid URL', 'utf-8'))
	else:
		soup = bs(html_file, 'lxml')
		soup = soup.prettify()
		client.send(bytes(soup, 'utf-8'))
		
def stop_server():
	client.close()
	sock.close()

def tcp_server(IP = '127.0.0.1', PORT = 8080):
	clear()
	print('**STARTING SERVER**')
	print('IP:', IP)
	print('PORT:', PORT)
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((IP, PORT))
	sock.listen(5)
	while True:
		try:
			global client
			client, addr = sock.accept()
			identify(addr)
			print('Connected from', addr)
		except KeyboardInterrupt:
			stop_server()
			break
		else:
			tcp_recv(client)

def create():
	while True:
		try:
			IP = input('IP address: ')
			PORT = int(input('PORT: '))
		except ValueError:
			print('PORT must be without letters')
			continue
		else:
			tcp_server(IP, PORT)


#=================================SQLITE===========================================


persons = []

class Person:
	def __init__(self, name, surname, job, salary):
		self.name = name
		self.surname = surname
		self.job = job
		self.salary = salary
	
def creating():
	conn = db.connect('persons.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE person(
			id integer PRIMARY KEY AUTOINCREMENT,
			name text,
			surname text,
			job text,
			salary integer
		)""")

def get_info():
	name = input("What is your name? ")
	surname = input('What is your surname? ')
	persons.append(surname)
	while True:
		conf = input("Have you got any job? ")
		if 'y' in conf:
			job = input('What kind of job do you have? ')
			salary = input('How much they pay for you? ')
			person = Person(name, surname, job, salary)
			insert(person)
			break
		elif 'n' in conf:
			print('Come back when you will get a job, bye')
			break
		else:
			print('"yes" or "no"')
			continue

def insert(p):
	conn = db.connect('persons.db')
	c = conn.cursor()
	c.execute("""INSERT INTO person(name, surname, job, salary)
			values(?, ?, ?, ?)""", (p.name, p.surname, p.job, p.salary))


#=====================================REGISTRATION===================================


class User:
	def __init__(self, nick, password):
		self.nick = nick 
		self.password = password

def acc_db():
	conn = db.connect('accounts.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE users(
			id integer PRIMARY KEY AUTOINCREMENT,
			nick text,
			password text
		)""")
	conn.commit()
	conn.close()

def new_acc(user):
	conn = db.connect('accounts.db')
	c = conn.cursor()
	while True:
		try:
			c.execute("""INSERT INTO users(nick, password)
				VALUES(?, ?)""", (user.nick, user.password))
			conn.commit()
			conn.close()
			break
		except db.OperationalError:
			acc_db()


def sing_up():
	print('**CREATING NEW ACCOUNT**')
	nick = input("Enter your nickname: ")
	password = input('Create a new password: ')
	conf = input("Repeat the password: ")
	if password == conf:
		user = User(nick, password)
		new_acc(user)
		clear()
	sing_in()

def sing_in():
		nick = input('Enter your nick: ')
		conn = db.connect('accounts.db')
		c = conn.cursor()
		c.execute('SELECT * FROM users')
		res = c.fetchall()
		x = 0
		while x <= 5:
			for i in res:
				if i[1] == nick:
					while True:
						password = input('Password: ')
						c.execute('SELECT * FROM users where nick = (?)', (nick,))
						res = c.fetchall()
						if res[0][2] == password:
							print('Welcome')
							break
						else:
							print('Wrong password')
							continue
				else:
					print('No user found')
					x += 1
					continue			

				

while True:
	acc = input('Do you have an account? ')
	if 'n' in acc:
		sing_up()
		break
	elif 'y' in acc:
		sing_in()
		break
	else:
		print('"yes" or "no"')
		continue


#====================================================================================


commands = ['insert', 'list', 'run server']
while True:
	command = input(">> ")
	if command == 'insert':
		direc = os.listdir()
		if 'persons.db' not in direc:
			creating()
		else:
			get_info()
	elif command == 'list':
		print('Persons you inserted today:')
		for i in persons:
			print(i.surname)
		continue
	elif command == 'clear' or command == 'cls':
		clear()
	elif command == 'run server':
		create()
	elif command == 'help':
		for i in commands:
			print(i)
	else:
		print('No command found')
		continue