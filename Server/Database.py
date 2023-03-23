import connexion as dbconnect


class Database:
    def __init__(self):
        self.__cursor = dbconnect.db.cursor()

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
    #TODO:Récupération des salons publics disponibles
    #def get_chatlist(self):
        #sql = "SELECT  FROM discord.messages WHERE salon_id = %s ORDER BY messagetime DESC "
        #self.__cursor.execute(sql, [salon_id])
        #return self.__cursor.fetchall()
    #TODO:Récuperer les fonctions créer par nicolas
    #Inscription
    #Connexion

    def verif_mail(self,mail):
        sql="SELECT * FROM utilisateurs WHERE email = %s"
        self.__cursor.execute(sql,mail)
        return self.__cursor.fetchall()


