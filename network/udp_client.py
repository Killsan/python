import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'connected', ('127.0.0.1', 8888))
#(<ip>, <port>); (unix.sock)
