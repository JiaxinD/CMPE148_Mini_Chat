from pymysql import connect
from config import *


class DB(object):
    #database management

    def __init__(self):
        self.conn= connect(host= DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                           )

        #get cursor
        self.cursor = self.conn.cursor()





    def close(self):
        #release database resource
        self.cursor.close()
        self.conn.close()




    def get_one(self,sql):
        #use sql find user info

        #use sql
        self.cursor.execute(sql)


        #get search result
        query_result = self.cursor.fetchone()

        #check condition
        if not query_result:
            return None

        #get  name string
        fileds = [filed[0] for filed in self.cursor.description]


        #use data and string

        return_data = {}

        for filed, value in zip(fileds,query_result):
            return_data[filed] = value

        return return_data


if __name__ == '__main__':
    db = DB()
    data = db.get_one("select * from users WHERE user_name='user2'")
    print(data)
    db.close()