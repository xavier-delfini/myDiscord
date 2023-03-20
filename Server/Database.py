import connexion as dbconnect
class Database:
    def __init__(self):
            self.__cursor=dbconnect.db.cursor()
    def create_item_in_database(self,message,user_id):
        import time
        if user_id !="" and message !="":
            command = "INSERT INTO discord.messages(message,sender_id) VALUES(%s,%s)"
            values = (message,user_id)
            self.__cursor.execute(command, values)
            dbconnect.db.commit()
        else:
            return "No Values"