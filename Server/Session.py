import threading
from _thread import *
import sys
import Database as db
class Session:
    def __init__(self,objet):
        self.__id=threading.get_ident()
        self.__session_objet=objet
       #self.__user_id=#Identifiant de l'utilisateur dans la base de donnée (différent de celui de session)
        self.__session_objet.send(self.__id)#Envoie de l'identifiant de connexion(ID du thread)
        self.__db=db.Database()
    def print_id(self):
        return self.__id

    def __identification(self):
        # Toutes les requêtes lorsque l'utilisateur est authentifié
        # doivent normalement commencer par l'id de connexion
        # afin d'éviter l'envoie de requêtes indésirables
        id = self.__session_objet.recv(16)
        if id == self.__id:
            return 1
        else:
            return 0

    def Main_Session(self):
        while True:
            if self.__identification()==1:
                commande=self.__session_objet.recv(1024)
                match commande:
                    case "GetMessage":
                        self.__GetMessage()
                    case "SentMessage":
                        self.__SentMessage()
                    case "Disconnect":
                        self.__Disconnect()
            else:
                break
        if self.__identification()==1:
            return 0
        else:
            return 4#L'utilisateur n'a pas envoyer l'ID de session(Potentiel tentative d'exploit)
    def __GetMessage(self):
        id = self.__session_objet.recv(1001)  # Récupération de l'id du salon
        self.__db.get_messages(int(id))
        self.__session_objet.sendall()
    #def __SentMessage(self):

    def __Disconnect(self):
        sys.exit()


