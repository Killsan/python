import sqlite3 as db
from employee import Employee

p1 = Employee('Elliot', 'Anderson', 'reversflash47')
p2 = Employee('Marshall', 'Methers', 'marshall7')


conn = db.connect('employee.db')
c = conn.cursor()

c.execute("""CREATE TABLE employee(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name text,
		sername text	
	)""")

c.execute("""CREATE TABLE jobs(
		id INTEGER PRIMERY KEY,
		sername text,
		job text DEFAULT null,
		FOREIGN KEY(id) REFERENCES employee(id),
		FOREIGN KEY(sername) REFERENCES employee(sername)
	)""")

# c.execute('INSERT INTO employee(name, sername) VALUES("Kirill", "Zhurov")')
# c.execute('INSERT INTO employee(name, sername) VALUES("John", "Lucas")')
# c.execute('INSERT INTO employee(name, sername) VALUES("Marshall", "Methers")')
# c.execute('INSERT INTO employee(name, sername) VALUES("Slim", "Shady")')
# c.execute('INSERT INTO employee(name, sername) VALUES("Elliot", "Anderson")')

conn.commit()
conn.close()