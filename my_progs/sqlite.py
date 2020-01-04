import os
import sqlite3 as db

os.system('clear')
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
		loc = os.getcwd()
		if 'C:' in loc or 'D:' in loc:
			os.system('cls')
		else:
			os.system('clear')
	else:
		print('No command found')
		continue