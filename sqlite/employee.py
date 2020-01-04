class Employee:
	def __init__(self, name, surname, addr):
		self.name = name
		self.surname = surname
		self.addr = addr

	@property
	def info(self):
		return"name: {}\n surname: {}\n email: {}".format(self.name, self.surname, self.addr)

p1 = Employee('Kirill', 'Zhurov', 'reversflash47')
print(p1.info)