# coding: utf-8

import socket
import pickle
import time
from Client.parameters import \
    constant as c  # Importation des constantes SERVER_IP et SERVER_PORT(déclarer comme constantes puisque ces valeurs ne sont pas censer changer en cours d'execution dans notre cas


# TODO:Method recup id salon, chercher un salon privée par mot de passe,créer un salon
class ClientCommands:
    def __init__(self):
        self.__session_id = -1
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((c.SERVER_IP, c.SERVER_PORT))
        print("Connection on {}".format(c.SERVER_PORT))

    def get_session_id(self):
        print("Réception id")
        self.__session_id = int.from_bytes(self.__socket.recv(1024), byteorder='big')
        print(self.__session_id)

    def authentification_with_server(self):
        # Envoi de l'id de session a chaque commande afin d'authentifier la requête
        time.sleep(1)
        session_id = self.__session_id.to_bytes(2, 'big')
        self.__socket.send(session_id)
        time.sleep(1)

    def verif_email(self, mail):
        print("vérif_mail")
        self.__socket.send(bytes("VerifMail", "utf-8"))
        time.sleep(0.5)
        self.__socket.send(bytes(mail, "utf-8"))

    def get_salon_messages(self, salon_id):
        self.authentification_with_server()
        # Envoi de la commande GetMessage
        print("Envoie commande getmessage")
        self.__socket.send(bytes("GetMessage", "utf-8"))
        time.sleep(1)

        # Envoie identifiant salon
        print("Envoie id salon")
        salon_id = salon_id.to_bytes(2, 'big')
        print(salon_id)
        self.__socket.send(salon_id)
        time.sleep(1)

        # Reception données messages
        Data = self.__socket.recv(10024)
        print(Data)
        time.sleep(1)

        receved_string = pickle.loads(Data)
        print(list(receved_string))

    # def get_user_id

    def send_message(self, session_id, user_id, message, salon_id):
        self.authentification_with_server()
        self.__socket.send(bytes("SendMessage", "utf-8"))
        time.sleep(1)
        data = pickle.dumps([message, user_id, salon_id])
        self.__socket.send(data)
        time.sleep(1)

    def disconnect(self, session_id):
        if session_id is not None:
            self.authentification_with_server()
            self.__socket.send(bytes("Disconnect", "utf-8"))
            time.sleep(1)

    def user_connexion(self, mail, password):
        # TODO:Password à hashé
        print("Envoie requete")
        self.__socket.send(bytes("connexion", "utf-8"))
        time.sleep(1)
        print("Envoie infos")
        self.__socket.send(pickle.dumps((mail, password)))
        print("Attente reception infos")
        connexion_response = self.__socket.recv(512)
        print("Données recu :", connexion_response)
        if connexion_response == b'Sucessed':
            self.get_session_id()
            return 1
        else:
            return 0

    def user_creation(self, prenom, nom, mail, password):
        print(password)
        user_infos = pickle.dumps((prenom, nom, mail, password))
        self.__socket.send(bytes("user_create", "utf-8"))
        time.sleep(1)
        self.__socket.send(user_infos)
        result = self.__socket.recv(512)

        print(result)
        if result == b'Account Created':
            self.get_session_id()
            return 1
        elif result == b'Failed':
            return 2

    def getSalonList(self):
        self.authentification_with_server()
        self.__socket.send(bytes("GetSalonList", "utf-8"))
        received_data = self.__socket.recv(1024)
        received_data = pickle.loads(received_data)
        print(received_data)
        return received_data

    def SearchPrivateSalon(self, passcode):
        self.authentification_with_server()
        self.__socket.send(bytes("SearchPrivateSalon", "utf-8"))
        time.sleep(1)
        self.__socket.send(bytes(passcode, "utf-8"))
        print("Reception résultat recherche salon")
        salon = self.__socket.recv(1024)
        salon = pickle.loads(salon)
        return salon

    def CreateSalon(self, name, accessibility=0, passcode=None):
        self.authentification_with_server()
        self.__socket.send(bytes("CreateSalon", "utf-8"))
        time.sleep(1)
        data = pickle.dumps([name, accessibility, passcode])
        self.__socket.send(data)
        result = self.__socket.recv(512)
        if result == b'Ok':
            return 1
        else:
            return 2

# a = ClientCommands()
# id = a.get_session_id()
# a.get_salon_messages(id, 1)
# a.send_message(id, 1, "Test_Objet", 1)
# a.disconnect(id)
# socket.close()
