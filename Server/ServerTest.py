# coding: utf-8
import socket

from Database import Database as db
import pickle
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        #Utilisateur authentifié
        socket.listen(5)
        client, address = socket.accept()
        print("{} connected".format(address))
        #endingmessage=bytes("End Of Transmission","utf-8")

        #L'utilisateur demande de consulter un salon
        send_message = db()
        messages=send_message.get_messages(1)
        bytes_array = pickle.dumps(messages)
        client.send(bytes_array)
        print(bytes_array)
        #endingmessage_bytes=pickle.dumps(endingmessage)
        #client.send(endingmessage_bytes)

        client.close()
#stock.close()
