import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connections = []
    def __init__(self, ip, port):
        self.sock.bind((ip, port))
        self.sock.listen()

    # send msg, if no msg break, else send
    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1], "disconnected"))
                self.connections.remove(c)
                c.close()
                break

    # connection and address should be accept
    def run(self):
        while True:
            c,a = self.sock.accept()
            cThread = threading.Thread(target=self.handler,args=(c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ':' + str(a[1], "connected"))

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""),'utf-8'))

    def __init__(self,address,port):
        self.sock.connect((address, port))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(data)

if __name__ == '__main__':
    if (len(sys.argv)>1):
        client = Client(sys.argv[1], 1000)
    else:
        server = Server('0.0.0.0', 1000)
        server.run