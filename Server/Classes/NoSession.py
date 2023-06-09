from Server.Classes import Database as db
import pickle
#Fini
class NoSession:
    def __init__(self, objet):
        # Timeout.__init__(self,is_session)
        self.__client_objet = objet
        self.__db = db.Database()

    def Main(self):
        while True:
            command = self.__client_objet.recv(512)
            match command:
                case b'connexion':
                    mail_pass = self.__client_objet.recv(2048)
                    mail_pass_list = pickle.loads(mail_pass)
                    self.__connexion(mail_pass_list[0], mail_pass_list[1])
                    break
                case b'user_create':
                    user = self.__client_objet.recv(4096)
                    user = pickle.loads(user)
                    print(user)
                    if self.__db.verif_mail(user[2]) == 1:
                        self.__create_user(user[0], user[1], user[2], user[3])
                        print(user)
                        self.__client_objet.send(bytes("Account Created", "utf-8"))
                    else:
                        print("Failed")
                        self.__client_objet.send(bytes("Failed", "utf-8"))
                        break

    def __create_user(self, prenom, nom, mail, password):
        self.__db.user_creation(prenom, nom, mail, password)

    def __connexion(self, mail, password):
        # TODO:récupération mail password, envoie id d'utilisateur,démarrage session
        if self.__db.user_connexion(mail, password) == 1:
            print("Vérif ok")
            print("Envoie infos")
            self.__client_objet.send(bytes("Sucessed", "utf-8"))

            from Server.Classes.Session import Session
            print("Récupération de l'id de session")
            print(self.__db.get_user_id([mail]))
            connected = Session(self.__client_objet, self.__db.get_user_id([mail]))
            print("Lancement session depuis NoSession")
            connected.main_Session()
        else:
            self.__client_objet.send(bytes("Failed", "utf-8"))
