bag = []
while True:
    confirm = input("Did you find something? ")
    if 'y' in confirm and len(confirm) <= 3:
        stuf = input("What? ")
        bag.append(stuf)
        continue
    elif 'n' in confirm and len(confirm) <= 2:
        print('ok')
        break
    else:
        continue
confirm0 = input('Do you wanna see what you just found? ')
if 'y' in confirm0 and len(confirm) <= 3:
    print('------------------------------------------------------------------------------')
    for i in bag:
        print(i)
    print('------------------------------------------------------------------------------')
else:
    print("Whatever")