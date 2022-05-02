


class SocketWrapper(object):
    #socket wrap
    def __init__(self,sock):
        self.sock = sock


    def receive_data(self):
        #receive data and encode to string
        try:
            return self.sock.recv(512).decode('utf-8')
        except:
            return ""

    def send_data(self,message):
        # encode string and sent to client
        return self.sock.send(message.encode('utf-8'))


    def close(self):
        #close socket
        self.sock.close()