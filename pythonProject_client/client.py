from interface_login import *
from request_protocol import RequestProtocol
from client_socket import ClientSocket
from threading import Thread
from config import *
from tkinter.messagebox import showinfo
from interface_Chat import WindowChat
import sys

class Client(object):

    def __init__(self):
        #inital client

        #initial loging interface
        self.window = WindowLogin()
        self.window.on_reset_click(self.clear_inputs)
        self.window.on_login_click((self.send_login_data))
        self.window.on_window_closed(self.exit)


        #initial chat interface

        self.window_chat = WindowChat()
        self.window_chat.withdraw()
        self.window_chat.on_send_click(self.send_chat_data)
        self.window_chat.on_window_close(self.exit)



        #create  client  socket



        self.conn = ClientSocket()


        #message function

        self.response_handle_function = {}
        self.register(RESPONSE_LOGIN_RESULT,self.response_login_handle)
        self.register(RESPONSE_CHAT,self.response_chat_handle)

        # self.response_handle_function[RESPONSE_LOGIN_RESULT] = self.response_login_handle
        # self.response_handle_function[RESPONSE_CHAT] = self.response_chat_handle
        #online user account name
        self.username = None

        #program running switch
        self.still_running = True

    def register(self,request_id, handle_function):
        self.response_handle_function[request_id] = handle_function

    def startup(self):
        self.conn.connect()

        Thread(target=self.response_handle).start()

        self.window.mainloop()



    def clear_inputs(self):
        #clear textbox content
        self.window.clear_username()
        self.window.clear_password()

    def send_login_data(self):
        #sent login info to server

        #get user inputs username and password

        username = self.window.get_username()
        password = self.window.get_password()

        #generate login protocol
        request_text = RequestProtocol.request_login_result(username,password)


        #sent to server text
        print('sent to server text is :  >>> ' + request_text )

        self.conn.send_data(request_text)
        # recv_data = self.conn.receive_data()
        # print(recv_data)


    def send_chat_data(self):
        #get textbox info sent to server
        message = self.window_chat.get_inputs()
        print('a %s a' %message)
        self.window_chat.clear_input()

        #joint protocol string
        request_text = RequestProtocol.request_chat(self.username,message)

        #send message
        self.conn.send_data(request_text)

        #show content in chat area
        self.window_chat.append_message('Mine' ,message)


    def response_handle(self):
        # receive server data
        while self.still_running:
            #get server data
            receive_data = self.conn.receive_data()
            print(("reveive server info :  " + receive_data))

            #analysis data
            response_data = self.parse_response_data(receive_data)

            # working according different type data

            handle_function = self.response_handle_function[response_data['response_id']]

            if handle_function:
                handle_function(response_data)

            # if response_data['response_id'] == RESPONSE_LOGIN_RESULT:
            #     self.response_login_handle(response_data)
            # elif response_data['response_id'] == RESPONSE_CHAT:
            #     self.response_chat_handle(response_data)

    @staticmethod
    def parse_response_data(recv_data):
        #login info    1001|0 OR 1|nickname|account
        # chat info      1002| nickname |message

        response_data_list = recv_data.split(DELIMITER)

        response_data = {}
        response_data['response_id'] = response_data_list[0]

        if response_data['response_id'] == RESPONSE_LOGIN_RESULT:
            response_data['result'] = response_data_list[1]
            response_data['nickname'] = response_data_list[2]
            response_data['username'] = response_data_list[3]

        elif response_data['response_id'] == RESPONSE_CHAT:
            response_data['nickname'] = response_data_list[1]
            response_data['message'] = response_data_list[2]

        return response_data


    def response_login_handle(self,response_data):
        # login response
        print('receive Login  message >> ', response_data)
        result = response_data['result']
        if result == '0':
            showinfo('Warning', 'Login Fail :  account or password wrong!!!!')

            return
        #login success , get user info
        nickname = response_data['nickname']
        self.username = response_data['username'] #svae online user account
        showinfo('Congratulations' , 'Login success')
        # print('%s ,    nickname : %s >>>>>>>>>>>> login success' % (username,nickname) )

        #show chat interface

        self.window_chat.set_title(nickname)
        self.window_chat.update()
        self.window_chat.deiconify()


        #hide login interface
        self.window.withdraw()

    def response_chat_handle(self,response_data):
        # chat response
        print("receice Chat messahe >>>" , response_data)
        sender = response_data['nickname']
        message = response_data['message']
        self.window_chat.append_message(sender,message)

    def exit(self):
        #quit program
        self.still_running = False  # stop child process
        self.conn.close() #close socket
        sys.exit(0)


if __name__ == '__main__':
    client = Client()
    client.startup()