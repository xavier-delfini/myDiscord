import threading
from _thread import *
import sys
import Database as db


class Session:
    def __init__(self, objet):
        self.__id = threading.get_ident()
        self.__session_objet = objet
        # self.__user_id=#Identifiant de l'utilisateur dans la base de donnée (différent de celui de session)
        self.__session_objet.send((self.__id).to_bytes(2,'big'))  # Envoie de l'identifiant de connexion(ID du thread)
        self.__db = db.Database()

    def print_id(self):
        print("id stocké en objet")
        print(self.__id)
        return self.__id

    def __identification(self):
        # Toutes les requêtes lorsque l'utilisateur est authentifié
        # doivent normalement commencer par l'id de connexion
        # afin d'éviter l'envoie de requêtes indésirables
        id = self.__session_objet.recv(512)
        id=int.from_bytes(id,byteorder='big')
        if id == self.__id:
            return 1
        else:
            return 0

    def Main_Session(self):
        while True:
            if self.__identification() == 1:
                commande = str(self.__session_objet.recv(1024))
                print(commande)
                match commande:
                    case "b'GetMessage'":
                        self.__GetMessage()
                    #case "SentMessage":
                        #self.__SentMessage()
                    case "b'Disconnect'":
                        self.__Disconnect()
                    #case "VocalChat":
                        #self.__VocalChat()
                    case _:
                        print("Aucune commande n'a été envoyer")

    def __GetMessage(self):
        import pickle
        print("Récupération id")
        id = self.__session_objet.recv(1001)# Récupération de l'id du salon
        print(id)
        print("compressions des données réçu")
        bytes_array = pickle.dumps(self.__db.get_messages(int.from_bytes(id,byteorder='big')))
        print(bytes_array)
        self.__session_objet.send(bytes_array)
        
    #def __VocalChat(self):
    # def __SentMessage(self):

    def __Disconnect(self):
        sys.exit()

