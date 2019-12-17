import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #choosing protocol
#DGRAM -- udp protocol
sock.bind(('127.0.0.1', 8888)) #reserving port on the machine
result = sock.recv(1024) #getting message from the network
print('Hello, bitch', result.decode('utf-8'))
sock.close()
