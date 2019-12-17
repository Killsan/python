class person:
	def __init__(self, name=None, sername=None):
		self.name = name
		self.sername = sername
		if sername == None:
			print(name)
		else:
			print(name, sername)

person('Kirill', 'Zhurov')