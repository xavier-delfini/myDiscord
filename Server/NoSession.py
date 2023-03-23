import Database as db
import threading
import time
import pickle
from Timeout import Timeout
from parameters import constant as c


class NoSession(Timeout):
    # TODO:A finir
    def __init__(self, objet):
        super().__init__(self)
        self.__client_objet = objet
        self.__db = db.Database()

    def Main(self):
        while True or self.timeout_connexion != 1:
            command = self.__client_objet.recv(512)
            pickle.loads(command)
            self.new_last_response()
            match command[0]:
                case b'connexion':
                    mail_pass = self.__client_objet.recv(512)
                    mail_pass_list = pickle.loads(mail_pass)
                    self.__connexion(mail_pass_list[0], mail_pass_list[1])
                case b'user_create':
                    user = self.__client_objet.recv(512)
                    mail_pass_list = pickle.loads(user)
                    if self.__db.verif_mail(user[2]):
                        self.__create_user(user[0], user[1],user[2],user[3])
                        self.__client_objet.send(bytes("Account Created","utf-8"))
                    else:
                        self.__client_objet.send(bytes("Failed","utf-8"))
        return 1

    def __create_user(self, prenom, nom, mail, password):


    def __connexion(self, mail, password):
        # TODO:récupération mail password, envoie id d'utilisateur,démarrage session
        if self.__db.user_connexion(mail, password) == 1:
            self.__client_objet.send(bytes("Sucessed","utf-8"))
            from Session import Session
            self.__db.get_user_id(mail)
            connected = Session(self.__client_objet)
            connected.Main_Session()
        else:
            self.__client_objet.send(bytes("Failed","utf-8"))

