from Server.parameters import SQL_Connexion as dbconnect


#TODO:Method recup id salon, chercher un salon privée par mot de passe,créer un salon
class Database:

    def __init__(self):
        self.__cursor = dbconnect.db.cursor()
    #-------Salon------
    #TODO:def search_private_salon(self,passcode):

    #TODO:def get_salon_ist(self):#Récupération des salons publics disponibles
        #sql = "SELECT  FROM discord.messages WHERE salon_id = %s ORDER BY messagetime DESC "
        #self.__cursor.execute(sql, [salon_id])
        #return self.__cursor.fetchall()

    #------Messages-------
    def add_message_to_database(self, message, user_id, salon):#1 utilisateur 2 classe session 3 utilisateur
        if user_id != "" and message != "" and salon != "":
            command = "INSERT INTO discord.messages(message,sender_id,salon_id) VALUES(%s,%s,%s)"
            values = (message, user_id,salon)
            self.__cursor.execute(command, values)
            dbconnect.db.commit()
        else:
            return "No Values"

    def get_messages(self, salon_id):#Utilisateur
        if isinstance(salon_id, int):
            sql = "SELECT * FROM discord.messages WHERE salon_id = %s ORDER BY messagetime DESC "
            self.__cursor.execute(sql, [salon_id])
            return self.__cursor.fetchall()
        else: return "Le numéro de salon est incorrect"


    #------Création de comptes-------
    def verif_mail(self,mail):
        print(mail)
        sql="SELECT * FROM utilisateurs WHERE email = %s"
        self.__cursor.execute(sql, [mail])
        if self.__cursor.fetchall():
            return 2
        else:
            return 1
    def user_creation(self,prenom,nom,mail,password):
        print("insert")
        command="INSERT INTO utilisateurs (prenom, nom, email, motdepasse) VALUES (%s, %s, %s, %s)"
        print("values:",prenom,nom,mail,password)
        values=(prenom,nom,mail,password)
        self.__cursor.execute(command,values)
        dbconnect.db.commit()

    #-------Connexion------
    def get_user_id(self,mail):
        command="SELECT id from utilisateurs WHERE email=%s"
        values=(mail)
        self.__cursor.execute(command,values)
        return self.__cursor.fetchone()
    def user_connexion(self,mail,password):
        command="SELECT * FROM utilisateurs WHERE email=%s AND motdepasse=%s"
        values=(mail,password)
        self.__cursor.execute(command,values)
        result=self.__cursor.fetchall()
        if result:
            return 1
        else:
            return 2
