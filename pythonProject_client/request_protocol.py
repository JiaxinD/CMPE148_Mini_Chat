from config import *


class RequestProtocol(object):

    @staticmethod
    def request_login_result(username,password):
        #0001|user1|123456  , type|account|password
        return DELIMITER.join([REQUEST_LOGIN, username, password])


    @staticmethod
    def request_chat(username,message):
        #0002|user1|xxxxxxx     ,  type|account|messages
        return DELIMITER.join([REQUEST_CHAT,username,message])