import socket
import time
import pickle   
HEADERSIZE = 10
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
while True:
    client, address = sock.accept()
    print(f"Connection from {address} has been established.")
    msg = "Welcome to the hell!"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    #client.send(bytes(msg,"utf-8"))
    while True:
        try:
            print('get over here')
        except KeyboardInterrupt:
            client.close()
            sock.close()
        else:
            time.sleep(3)
            msg =  f'Time is {time.time()}'
            msg = f'{len(msg):<{HEADERSIZE}}' + msg
            client.send(bytes(msg,"utf-8"))