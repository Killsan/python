import socketserver
class ThreadingTCPServer(socket.server.ThreadingMixIn, socketserver.TCPServer):
    pass
class EchoTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print('addres {}', format(self.client_address[0]))
        print('data {}', format(data.decode()))
        self.request.sendall(data)
if __name__ == '__main__':
    with ThreadingTCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve.forever()