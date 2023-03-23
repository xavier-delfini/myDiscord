import time
from parameters import constant as c
class Timeout:
    def __init__(self,session):
        self.__wait_time_receving,self.__wait_connexion=self.__get_constants()
        self.__sessionOpen=session
    def __get_constants(self):
        match self.__sessionOpen:
            case 0:
                return c.NO_SESSION_TIMEOUT_WAIT_RECEVING, c.NO_SESSION_TIMEOUT_CONNEXION

            #case 1:

    def __new_last_response(self):
        self.__last_response = time.time()
    def __timeout_connexion(self):
        if (time.time()-self.__last_response) > self.__wait_connexion:
            return 1
    def __timeout_request(self):
        if (time.time() -self.__last_response) > self.__wait_time_receving:
            return 1