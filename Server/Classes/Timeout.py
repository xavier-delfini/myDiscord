import time
from Server.parameters import constant as c
class Timeout:
    def __init__(self,session):
        self.__wait_time_receving,self.__wait_connexion=self.__get_constants()
        self.__sessionOpen=session
    def __get_constants(self):
        match self.__sessionOpen:
            case 0:
                return c.NO_SESSION_TIMEOUT_WAIT_RECEVING, c.NO_SESSION_TIMEOUT_CONNEXION
            case 1:
                return c.SESSION_TIMEOUT_WAIT_RECEVING, c.SESSION_TIMEOUT_CONNEXION

    def new_last_response(self):
        self.__last_response = time.time()
    def timeout_connexion(self):
        if (time.time()-self.__last_response) > self.__wait_connexion:
            return 1
    def timeout_request(self):
        if (time.time() -self.__last_response) > self.__wait_time_receving:
            return 1