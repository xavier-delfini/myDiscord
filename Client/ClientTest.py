# coding: utf-8

import socket
import pickle
import time

hote = "localhost"
port = 15555
# Test envoie de paquet limité a 64 caractères
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))
def get_session_id():
    print("Réception id")
    session_id=socket.recv(1024)
    print(session_id)
    return session_id

def authentification_with_server(session_id):
    #Envoie de l'id de session afin de pouvoir executer la commande
    socket.send(session_id)
    time.sleep(1)

def get_salon_messages(session_id,salon_id):
    authentification_with_server(session_id)
    #Envoie de la commande GetMessage
    socket.send(bytes("GetMessage","utf-8"))
    time.sleep(1)

    #Envoie identifiant salon
    socket.send((salon_id).to_bytes(2, 'big'))
    time.sleep(1)

    #Reception données messages
    Data=socket.recv(1500)
    print(Data)
    time.sleep(1)

    receved_string = pickle.loads(Data)
    print(list(receved_string))



id=get_session_id()
get_salon_messages(id,1)

#socket.close()
