import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # connections = []
    def __init__(self, ip, port):
        self.sock.bind((ip, port))
        self.sock.listen()

    # send msg, if no msg break, else send
    def handler(self, cnt, address):
        while True:
            msg = input(">>")
            msg = msg.encode()
            cnt.send(msg)
            data = cnt.recv(1024)
            data = data.encode()
            # for connection in self.connections:
            #     connection.send(data)
            if not data:
                print(str(address[0]) + ':' + str(address[1], "disconnected"))
                self.connections.remove(cnt)
                cnt.close()
                break

    # connection and address should be accept
    def run(self):
        while True:
            cnt,address = self.sock.accept()
            cThread = threading.Thread(target=self.handler,args=(cnt,address))
            cThread.daemon = True
            cThread.start()
            self.connections.append(cnt)
            print(str(address[0]) + ':' + str(address[1], "connected"))

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
            data = data.decode()
            msg = input(str(">>"))
            msg = msg.encode()
            if not data:
                break
            print(data)

if __name__ == '__main__':
    if (len(sys.argv)>1):
        client = Client(sys.argv[1], 1000)
    else:
        server = Server('192.168.1.104', 1000)
        server.run