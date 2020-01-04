import socket
import os
from bs4 import BeautifulSoup as bs

def clear():
	loc = os.getcwd()
	if 'C:' in loc or 'D:' in loc:
		os.system('cls')
	else:
		os.system('clear')

def tcp_client(IP = '127.0.0.1', PORT = 8080):
	clear()
	print('**CONNECTING**')
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((IP, PORT))
	while True:
		try:
			msg = input('--> ')
			sock.send(bytes(msg, 'utf-8'))
			res = sock.recv(2097152)
			res = res.decode('utf-8')
			file = open('index.html', 'w')
			file.write(res)
			file.close()
			with open('index.html', 'r') as index:
				if 'Invalid URL' in index.read():
					print('Invalid URL')
				else:
					print('Html code saved in "index.html"')
			break
		except BrokenPipeError:
			continue


def connect():
	while True:
		try:
			IP = input('IP address: ')
			PORT = int(input('PORT: '))
		except ValueError:
			print('PORT must be without letters')
			continue
		else:
			tcp_client(IP, PORT)
			break

# tcp_client()
connect()