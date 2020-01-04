import os
import socket
def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8888))
    sock.listen(5)
    while True:
        try:
            client, addr = sock.accept()
        except KeyboardInterrupt:
            sock.close()
            client.close()
            break
        else:
            while True:
                msg = client.recv(1024)
                result = msg.decode('utf-8')
                print(result)
def console():
    commands = ['exit', 'ls', 'pwd', 'cd', 'start server']
    while True:
        command = input('$ ')
        if command == 'cd' or command == ' cd' or command == 'cd ':
            path = input('$--> ')
            os.chdir(path)
        elif command == 'exit':
            break
        elif command == 'start server':
        	server()
        	continue
        elif command == 'pwd':
            print(os.getcwd())
            continue
        elif command == 'ls':
            print(os.listdir())
            continue
        else:
            for i in commands:
                print(i)
def log_in():
    nickname = open('name.txt', 'r')
    password = open('password.txt', 'r')
    name = input('Enter your name--> ')
    if name == nickname.read():
        confirm = input('Enter your password--> ')
        if confirm == password.read():
            print('welcome')
            console()
        else:
            print('Wrong password')
    else:
        print('Here is no nikcname like that')
# def sing_up():
#     login = open('password.txt', 'w')
#     nickname = input("Enter your username--> ")
#     name = open('name.txt', 'w')
#     name.write(nickname)
#     name.close()
#     password = input('Enter your password--> ')
#     login.write(password)
#     login.close()
#     password_confirm = input('Confirm your password--> ')
#     login = open('password.txt', 'r')
#     pass2 = login.read()     
#     if password_confirm == pass2:
#         print('ok') 
#     elif password_confirm != pass2:
#         print('Wrong')
#         login.close()
#         login = open('password.txt', 'w')
#         nickname = open('name.txt', 'w')
#         login.close()
#         nickname.close()
#     else:
#         print('Fuck')
def sing_up():
    login = open('password.txt', 'wr')
    text = input("Enter the pass--> ")
    print(text.read())
def ask():
    while True:
        try:
            confirm = input('Have you got an account? ')
            if confirm == 'y':
                log_in()
                break
            elif confirm == 'n':
                sing_up()
                break
            else:
                print('What the hell')
        except FileNotFoundError:
            print('no users in programm')
            sing_up()
server()
