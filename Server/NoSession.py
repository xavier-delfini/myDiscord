import Database as db
import threading
import time
import pickle
from parameters import constant as c
class NoSession:
    #TODO:A finir
    def __init__(self,objet):
        self.__last_response = time.time()
        self.__client_objet=objet
    def __new_last_response(self):
        self.__last_response = time.time()
    def __timeout_connexion(self):
        if self.__last_response > c.NO_SESSION_TIMEOUT_CONNEXION:
            return 1
    def __timeout_request(self):
        if self.__last_response > c.NO_SESSION_TIMEOUT_WAIT_RECEVING:
            return 1
    def Main(self):
        while True or self.__timeout_connexion==1:

    def create_user(self,prenom,nom,mail,password):
        array_user=pickle.dumps([prenom,nom,mail,password])

    def connexion(self,mail,password):

