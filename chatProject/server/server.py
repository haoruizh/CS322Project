import socket
import json
from threading import Thread

class Client(Thread):
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((ip,port))
        while True:
            a = input()
            self.client.send(a.encode("utf-8"))
            data = self.client.recv(1024)
            print(data.decode("uft8"))

class Server:
    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((ip,port))
        self.server.listen(5)
        # connection, address = self.server.accept()
        while True:
            connection, address = self.server.accept()
            client_thread = Thread(target=self.handle_sock, args=(connection,address))
            data = connection.recv(1024)
            print(data.decode("utf-8"))
            a = input("")
            print(data.decode("uft8"))
            client_thread.start()

    def handle_sock(self, connection, address):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        while True:
            data = connection.recv(1024)
            b = data.decode("utf-8")
            print(b)
            a = input("")
            self.connection.send(a.encode("utf8"))

if __name__ == '__main__':
    client = Client('127,0,0,1',10086).start()