import random

rand_mass = ['Hi','Hola', 'Ma man', "What's up?"]
print('-'*80)
print('Random shit:\n')
for i in rand_mass:
	print(i)
print('-'*80)

value = random.random()
print('random.random(): ' + str(value))

value = random.uniform(1, 10)
print('random.uniform(<val>, <val>): ' + str(value))

value = random.randint(1, 6)
print('random.randint(<val>, <val>): ' + str(value))

value = random.randint(1, 6)
print('random.randint(<val>, <val>): ' + str(value))

value = random.choice(rand_mass)
print('random.choice(<massiv>): ' + str(value))

value = random.choices(rand_mass, k=10)
print('random.choices(<massiv>, k=<how many>: ' + str(value))

value = random.choices(rand_mass, weights=[15, 20, 30, 40] ,k=10)
print('random.choices(<massiv>, weight=[], k=<how many>: ' + str(value))

value = list(range(1, 13))
print('list(range(<val>, <val>)): ' + str(value))

random.shuffle(value)
print('random.shuffle(massiv): ' + str(value))	

value = random.sample(value, k=5)
print('random.smaple(<massiv>, k=<val>: ' + value)