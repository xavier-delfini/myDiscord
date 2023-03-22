# coding: utf-8

import socket
import pickle
import time
from parameters import constant as c#Importation des constantes SERVER_IP et SERVER_PORT(déclarer comme constantes puisque ces valeurs ne sont pas censé changer en cours d'execution dans notre cas
class ClientCommands:
    def __init__(self):
        self.__socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((c.SERVER_IP, c.SERVER_PORT))
        print("Connection on {}".format(c.SERVER_PORT))
    def get_session_id(self):
        print("Réception id")
        session_id=self.__socket.recv(1024)
        print(session_id)
        return session_id

    def authentification_with_server(self,session_id):
        #Envoie de l'id de session a chaque commande afin d'authentifier la requête
        self.__socket.send(session_id)
        time.sleep(1)

    def get_salon_messages(self,session_id,salon_id):
        self.authentification_with_server(session_id)
        #Envoie de la commande GetMessage
        self.__socket.send(bytes("GetMessage","utf-8"))
        time.sleep(1)

        #Envoie identifiant salon
        self.__socket.send((salon_id).to_bytes(2, 'big'))
        time.sleep(1)

        #Reception données messages
        Data=self.__socket.recv(1500)
        print(Data)
        time.sleep(1)

        receved_string = pickle.loads(Data)
        print(list(receved_string))
    #def get_user_id

    def send_message(self,session_id, user_id, message, salon_id):
        self.authentification_with_server(session_id)
        self.__socket.send(bytes("SendMessage", "utf-8"))
        time.sleep(1)
        self.__socket.send(bytes(message, "utf-8"))
        time.sleep(1)
        self.__socket.send((user_id).to_bytes(2, 'big'))
        time.sleep(1)
        self.__socket.send((salon_id).to_bytes(2, 'big'))
        time.sleep(1)
        self.get_salon_messages(session_id, salon_id)

    #def send_message(session_id,message,salon_id):

    def disconnect(self,session_id):
        if session_id is not None:
            self.authentification_with_server(session_id)
            self.__socket.send(bytes("Disconnect", "utf-8"))
            time.sleep(1)


a=ClientCommands()
id=a.get_session_id()
a.get_salon_messages(id,1)
a.send_message(id,1,"Test_Objet",1)
a.disconnect(id)
#socket.close()
