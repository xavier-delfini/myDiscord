import threading
import time
import sys
import pickle
from Server.Classes import Database as db


#TODO:chercher un salon privée par mot de passe
class Session:
    def __init__(self, objet, user_id):
        print("Démmarage session ")
        self.__session_id = threading.get_ident()
        self.__user_id=user_id[0]
        self.__session_objet = objet
        print("Envoie id ", self.__session_id)
        # self.__user_id=#Identifiant de l'utilisateur dans la base de donnée (différent de celui de session)
        self.__session_objet.send(self.__session_id.to_bytes(2, 'big'))  # Envoie de l'identifiant de connexion(ID du thread)
        self.__db = db.Database()
    def __identification(self):
        # Toutes les requêtes lorsque l'utilisateur est authentifié
        # doivent normalement commencer par l'id de connexion(ID du thread dont la connexion est lié)
        # afin d'éviter l'envoie de requêtes indésirables
        id = self.__session_objet.recv(512)
        id = int.from_bytes(id, byteorder='big')
        if id == self.__session_id:
            return 1
        else:
            return 0

    def main_Session(self):
        while True:
            time.sleep(0.1)
            if self.__identification() == 1:
                commande = str(self.__session_objet.recv(1024))
                match commande:
                    case "b'GetMessage'":
                        self.__GetMessage()
                    case "b'SendMessage'":
                        print("Commande reçu")
                        self.__SendMessage()
                    case "b'GetSalonList'":
                        self.__GetSalonList()
                    case "b'Disconnect'":
                        self.__Disconnect()
                    case "b'SearchPrivateSalon'":
                        self.__SearchForPrivateSalon()
                    case "b'CreateSalon'":
                        self.__CreateSalon()
                    # case b'VocalChat':
                    # self.__VocalChat()
                    case _:
                        print("Aucune commande n'a été envoyer")

    def __GetMessage(self):
        print("Récupération id")
        id = self.__session_objet.recv(1001)  # Récupération de l'id du salon
        print("compressions des données réçu:")
        id=int.from_bytes(id, byteorder='big')
        bytes_array = pickle.dumps(self.__db.get_messages(id))
        print(bytes_array)
        self.__session_objet.send(bytes_array)

    # def __VocalChat(self):
    # def __SentMessage(self):

    def __Disconnect(self):
        sys.exit()

    def __SendMessage(self):

        message = self.__session_objet.recv(2048)
        print("Message reçu")
        message = pickle.loads(message)
        print(message)
        self.__db.add_message_to_database(message[0], self.__user_id, message[1])

    def __GetSalonList(self):
        bytes_array = pickle.dumps(self.__db.get_salon_list())
        print(bytes_array)
        self.__session_objet.send(bytes_array)

    def __SearchForPrivateSalon(self):
        passcode=self.__session_objet.recv(1024)
        print("reception du passcode")
        passcode=passcode.decode()

        result=self.__db.SearchForPrivateSalon([passcode])
        print("recherche dans la base de donnée")
        result=pickle.dumps(result)
        self.__session_objet.send(result)
        print("envoie du résultat")

    def __CreateSalon(self):
        salon = self.__session_objet.recv(1024)
        salon=pickle.loads(salon)
        if self.__db.CreateSalon(salon[0],salon[1],salon[2]) == 1:
            self.__session_objet.send(bytes("Ok","utf-8"))
        else:
            self.__session_objet.send(bytes("Already exist","utf-8"))
