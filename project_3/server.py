from server_socket import ServerSocket
from socket_wapper import SocketWrapper
from threading import Thread
from config import *
from response_protocol import *
from database import DB


class Server(object):
    # server core class
    def __init__(self):
        #create server socket
        self.server_socket = ServerSocket()


        #create request ID and function  related

        self.request_handle_function = {}
        self.register(REQUEST_LOGIN,self.request_login_handle)
        self.register(REQUEST_CHAT,self.request_chat_handle)

        # create dict to save current user info
        self.clients = {}

        #create database mangment object
        self.db = DB()

        #
        # self.request_handle_function[REQUEST_LOGIN] = self.request_login_handle
        # self.request_handle_function[REQUEST_CHAT] = self.request_chat_handle


    def register(self,request_id, handle_function):
        # regist  function in dict
        self.request_handle_function[request_id] = handle_function



    def startUP(self):
        # get client connect
        while True:
            print("waiting client connect to  server !!!!!")
            soc, addr = self.server_socket.accept()

            print(("got client  connect "))


            client_soc = SocketWrapper(soc)
            #
            # t = Thread(target= self.request_handle, args =(client_soc,))
            # t.start()
            Thread(target=lambda :self.request_handle(client_soc)).start()


            # close client
        # soc.close()

    def request_handle(self,client_soc):

        while True:
            # receive client data
            receive_data = client_soc.receive_data()
            if not receive_data:
                #not receive message when client close
                self.remove_offline_user(client_soc)
                client_soc.close()
                break

            # analysis data
            parse_data = self.parse_request_text(receive_data)


            # print("analysis data: %s" %parse_data)

            # call function according request type
            # if parse_data['request_id'] == REQUEST_LOGIN:
            #     self.request_login_handle()
            # elif parse_data['request_id'] == REQUEST_CHAT:
            #     self.request_chat_handle()


            handle_function = self.request_handle_function.get(parse_data['request_id'])
            if handle_function:
                handle_function(client_soc,parse_data)


            # use socket warp to generate object



            # print(mes)
            # client_soc.send_data("Server receive : " + mes)

    def remove_offline_user(self, client_soc):
        #client offline problem
        print("client offline !!!")
        for  username, info in self.clients.items():
            if info['sock'] == client_soc:
                print(self.clients)
                del  self.clients[username]
                print(self.clients)
                break

    def parse_request_text(self, text):
        #analysis client data
        # login info  :  0001/username/password
        # char info :  0002/username/message



        print("analysis client data :" + text)

        request_list = text.split(DELIMITER)
        # according to analysis type
        request_data ={}
        request_data['request_id'] = request_list[0]

        if request_data['request_id'] ==  REQUEST_LOGIN:
            #user request login
            request_data['username'] = request_list[1]
            request_data['password'] = request_list[2]

        elif request_data['request_id'] == REQUEST_CHAT:
            #user send chat message
            request_data['username'] = request_list[1]
            request_data['messages'] = request_list[2]

        return request_data

    def request_chat_handle(self,client_soc, request_data):
        #work on chat function
        print("receive chat message, ready to work with it ",request_data)

        #get message data

        username = request_data['username']
        messages = request_data['messages']
        nickname = self.clients[username]['nickname']
        #joint message text
        msg = ResponseProtocol.response_chat(nickname,messages)

        #send message to each online client
        for u_name , info in self.clients.items():
            if username == u_name:
                continue
            info['sock'].send_data(msg)

    def request_login_handle(self, client_soc, request_data):
        # work login data
        print('receive login data , ready to work with it')

        #get user account  and password
        username = request_data['username']
        password = request_data['password']

        #check  able or enable to login
        ret, nickname, username = self.check_user_login(username,password)

        # save current user info if success
        if ret == '1':
            self.clients[username] = {'sock': client_soc, 'nickname': nickname}



        # joint string which return to client
        response_text =  ResponseProtocol.response_login_result(ret,nickname,username)

        #send message to client
        client_soc.send_data(response_text)


    def check_user_login(self, username, password):
        # check user success login or not, return result (0:false , 1 : success) , nickname, account

        #check user info from database
        sql = "select * from users where user_name = '%s'" % username
        result = self.db.get_one(sql)

        # if no check result, user not exist , login fail
        if not result:
            return '0','', username


        #if password not match , login fail
        if password != result['user_password']:
            return '0','', username

        #esle login success

        return '1',result['user_nickname'], username

if __name__ == '__main__':
    Server().startUP()