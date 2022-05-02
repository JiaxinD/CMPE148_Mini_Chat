import socket
from config import *



class ClientSocket(socket.socket):
    
    def __init__(self):
        #setting TCP socket
        super(ClientSocket, self).__init__(socket.AF_INET,socket.SOCK_STREAM)
        
    def connect(self):
        super(ClientSocket, self).connect((SERVER_IP,SERVER_PORT))


    def receive_data(self):
        #receive data transfer to string
        return self.recv(512).decode('utf-8')

    def send_data(self,message):
        #receive string transfer to bytes
        return self.send(message.encode('utf-8'))