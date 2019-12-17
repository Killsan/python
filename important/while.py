while True:
    number = int(input('Enter the number '))
    if number < 48:
        print('The correct number is bigger then yours')
    elif number > 48:
        print('The correct number is smaller then yours')
    else:
        print('You are motherficker')
        break