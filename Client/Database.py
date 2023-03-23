import mysql.connector


class Database:
    def __init__(self):
        self.__user = 'root'
        self.__password = 'root'
        self.__host = '127.0.0.1'
        self.__db = 'Discord'
        self.__db = mysql.connector.connect(user=self.__user, password=self.__password, host=self.__host, database=self.__db)

    def db(self):
        return self.__db