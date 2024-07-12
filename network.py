import socket

class Network:
    """
    TODO: WIT.
    s.ab. responsible for connecting to the server. Apparently a re-usable class.
    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = "192.168.1.35"
        self.server = "172.20.10.2"
        self.port = 5555
        self.addr = (self.server, self.port)
        # ... save what the server returns to the client (currently "Connected")
        self.pos = self.connect()
        # print(self.id)

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

# DEBUG
# n = Network()
# print(n.send("Hello"))
# print(n.send("Working"))
