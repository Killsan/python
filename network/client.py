import os
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
while True:
	msg = input('killsan@root:~$ ')
	sock.send(bytes(msg, 'utf-8'))