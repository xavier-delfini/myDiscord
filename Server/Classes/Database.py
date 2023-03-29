from Server.parameters import SQL_Connexion as dbconnect


# TODO:Methode chercher un salon privée par mot de passe à tester
class Database:

    def __init__(self):
        self.__cursor = dbconnect.db.cursor()

    # -------Salon------
    def get_salon_list(self):  # Récupération des salons publics disponibles
        sql = "SELECT  * FROM discord.salon WHERE droit = 0"
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    # ------Messages-------
    def add_message_to_database(self, message, user_id, salon):  # 1 utilisateur 2 classe session 3 utilisateur
        if user_id != "" and message != "" and salon != "":
            command = "INSERT INTO discord.messages(message,sender_id,salon_id) VALUES(%s,%s,%s)"
            values = (message, user_id, salon)
            self.__cursor.execute(command, values)
            dbconnect.db.commit()
        else:
            return "No Values"

    def get_messages(self, salon_id):  # Utilisateur
        if isinstance(salon_id, int):
            sql = "SELECT messages.id, message, messagetime, discord.utilisateurs.nom  FROM discord.messages LEFT JOIN discord.utilisateurs ON messages.sender_id = utilisateurs.id WHERE salon_id = %s ORDER BY messagetime DESC"
            self.__cursor.execute(sql, [salon_id])
            return self.__cursor.fetchall()
        else:
            return "Le numéro de salon est incorrect"

    # ------Création de compte-------
    def verif_mail(self, mail):
        print(mail)
        sql = "SELECT * FROM utilisateurs WHERE email = %s"
        self.__cursor.execute(sql, [mail])
        if self.__cursor.fetchall():
            return 2
        else:
            return 1

    def user_creation(self, prenom, nom, mail, password):
        print("insert")
        command = "INSERT INTO utilisateurs (prenom, nom, email, motdepasse) VALUES (%s, %s, %s, %s)"
        print("values:", prenom, nom, mail, password)
        values = (prenom, nom, mail, password)
        self.__cursor.execute(command, values)
        dbconnect.db.commit()

    # -------Connexion------
    def get_user_id(self, mail):
        command = "SELECT id from utilisateurs WHERE email=%s"
        values = (mail)
        self.__cursor.execute(command, values)
        return self.__cursor.fetchone()

    def user_connexion(self, mail, password):
        command = "SELECT * FROM utilisateurs WHERE email=%s AND motdepasse=%s"
        values = (mail, password)
        self.__cursor.execute(command, values)
        result = self.__cursor.fetchall()
        if result:
            return 1
        else:
            return 2

    def SearchForPrivateSalon(self, passcode):
        sql = "SELECT * FROM discord.salon WHERE droit=1 and passcode=%s"
        value = (passcode)
        self.__cursor.execute(sql, value)
        result = self.__cursor.fetchall()
        if result:
            return result
        else:
            return 1

    def CreateSalon(self, name, accessibility=0, passcode=None):
        if self.__verifySalonName(name) == 1:
            sql = "INSERT INTO discord.salon(nom,droit,passcode) VALUES(%s,%s,%s)"
            values = (name, accessibility, passcode)
            self.__cursor.execute(sql, values)
            dbconnect.db.commit()
            return 1
        else:
            return 2

    def __verifySalonName(self, name):
        sql = "SELECT * FROM discord.salon WHERE nom=%s"
        values = ([name])
        self.__cursor.execute(sql, values)
        result = self.__cursor.fetchall()
        if result:
            return 2
        else:
            return 1


#test = Database()
#print(test.add_message_to_database("ABC",1,1))

