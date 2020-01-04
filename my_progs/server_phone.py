import socket
import os
import requests
import sqlite3 as db
from bs4 import BeautifulSoup as bs


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
			print('Connectid from', addr)
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

def create(name):
	conn = db.connect(name + '.db')
	c = conn.cursor()

	c.execute("""CREATE TABLE first(
			id integer PRIMARY KEY AUTOINCREMENT,
			name text,
			surname text
		)""")

	c.execute("""CREATE TABLE second(
			id integer PRIMARY KEY AUTOINCREMENT,
			surname text,
			job text,
			salary integer,
			FOREIGN KEY(id) REFERENCES first(id),
			FOREIGN KEY(surname) REFERENCES first(surname)
		)""")

	conn.commit()
	conn.close()	

def database(s):
	conn = db.connect(sqldb+'.db')
	c = conn.cursor()
	c.execute('INSERT INTO first(name, surname) VALUES(?, ?)', (s.name, s.surname))
	c.execute('INSERT INTO second(surname, job, salary) VALUES(?, ?, ?)', (s.surname, s.job, s.salary))
	conn.commit()
	conn.close()

def insert():
	name = input('Enter your name: ')
	surname = input('Enter your surname: ')
	confirm = input('Have you got a job? ')
	if 'y' in confirm:
		job = input('What kind of job you have? ')
		salary = input('How much they pay for you? ')
		surname = Person(name, surname, job, salary)
		persons.append(surname)
		database(surname)
	else:
		print('We need a humans with job, bye')


#=========================================================================

commands = ['insert', 'list', 'create database', 'run server']
while True:
	command = input(">> ")
	if command == 'insert':
		insert()
	elif command == 'list':
		for i in persons:
			print(i.surname)
		continue
	elif command == 'create database':
		sqldb = input('Enter the name of new database: ')
		create(sqldb)
	elif command == 'clear' or command == 'cls':
		clear()
	elif command == 'run server':
		create()
	elif command == 'help':
		for i in commands:
			pirnt(i)
	else:
		print('No command found')
		continue