import connexion as dbconnect
class Database:
    def __init__(self):
            self.__cursor=dbconnect.db.cursor()
    def create_item_in_database(self,message,user_id,salon):
        if user_id !="" and message !="" and salon!="":
            command = "INSERT INTO discord.messages(message,sender_id,salon_id) VALUES(%s,%s,%s)"
            values = (message,user_id)
            self.__cursor.execute(command, values)
            dbconnect.db.commit()
        else:
            return "No Values"
    def get_messages(self,salon_id):
        if isinstance(salon_id,int):
            sql="SELECT * FROM discord.messages WHERE salon_id = %s ORDER BY messagetime DESC "
            self.__cursor.execute(sql,[salon_id])
            return self.__cursor.fetchall()