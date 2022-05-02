from config import  *

class ResponseProtocol():
    #server response  format
    @staticmethod
    def response_login_result(result, nickName, userName):
        '''
        generate user login result string
        :param result:  value 0 : login Fail , value 1 : login success
        :param nickName:  user nickName , NULL if login fail
        :param userName:  use account name, NULL if  login fail
        :return: return  user login result protocol string
        '''

        return DELIMITER.join([RESPONSE_LOGIN_RESULT,result, nickName, userName])


    @staticmethod
    def response_chat(nickName, messages):
        '''
        generate user message stirng
        :param nickName:  message sender user name
        :param messages:   message
        :return: return user message string
        '''
        return DELIMITER.join([RESPONSE_CHAT, nickName , messages])