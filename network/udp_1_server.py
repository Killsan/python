import socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#DGRAM -- udp protocol
sock.bind(('127.0.0.1', 8888))
while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('This bitch says:', result.decode('utf-8'))