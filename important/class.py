class INTRODUCTION:
	def __init__(self, name, sername, age):
		self.name = name
		self.sername = sername
		self.age = age

	def hello(self):
		print('Hello, my name is ' + self.name)

	def culc(self):
		while True:
			try:
				quest = int(input("Enter the age you need: "))
			except ValueError:
				print('ONly numbers')
				continue
			else:
				if quest == self.age:
					print('We got it')
				else:
					print('Sorry, but we have no robot like that')
				break


# robot1 = INTRODUCTION()
# robot1.name = 'Robert'
# robot1.sername = 'Patternson'
# robot1.age = '21'

# robot2 = INTRODUCTION()
# robot2.name = 'Killsan'
# robot2.sername = 'Anderson'
# robot2.age = '54'

r1 = INTRODUCTION('Elliot', 'Anderson', 25)
r2 = INTRODUCTION('Mr', 'Robot', 55)


class Person:
	def __init__(self, name, sitting, age):
		self.name = name
		self.sitting = sitting
		self.age = age
		
	def sit_down(self):
		self.sitting = True
		print(self.name + ' gonna sit down')

	def stand_up(self):
		self.sitting = False
		print(self.name + ' gonna stand up')

	def check(self):
		if self.sitting == True:
			print(self.name, 'is sitting and he(she) is', self.age, 'years old')
		else:
			print(self.name, 'is staying and he(she) is', self.age, 'years old')

alis = Person('Alis', False, 99)
mark = Person('Mark', True, 10)

# alis.check()
# mark.check()
# mark.stand_up()
# alis.sit_down()
# mark.check()
# alis.check()

# print('Thats how mafia works')


