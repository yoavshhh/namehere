import socket

class Peer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))

    def send(self, data, target):
        self.socket.sendto(data.encode(), target)

    def receive(self):
        data, addr = self.socket.recvfrom(1024)
        return data.decode(), addr