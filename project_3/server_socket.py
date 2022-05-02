import socket
from config import *


class ServerSocket(socket.socket):

    def __init__(self):
        # set  tupe to TCP
        super(ServerSocket,self).__init__(socket.AF_INET, socket.SOCK_STREAM)

        # binding address and port
        self.bind((SERVER_IP, SERVER_PORT))

        #set up listen mode
        self.listen(128)


