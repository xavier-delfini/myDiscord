# coding: utf-8

import socket
import pickle
import time
from Client.Classes.ClientCommands import ClientCommands

Test = ClientCommands()
Test.user_connexion("a", "a")
#print(Test.get_salon_messages(1))
#Test.getSalonList()
print(Test.SearchPrivateSalon("a"))
#TODO:Test envoie messages
#TODO:Test recup salon

'''
hote = "localhost"
port = 15555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))
def get_session_id():
    print("Réception id")
    session_id=socket.recv(1024)
    print(session_id)
    return session_id

#def get_user_id


def send_message(session_id,user_id,message,salon_id):
    # TODO:Simplifié le code (réduire le nombrde d'envois)
    authentification_with_server(session_id)
    socket.send(bytes("SendMessage", "utf-8"))
    time.sleep(1)
    socket.send(bytes(message,"utf-8"))
    time.sleep(1)
    socket.send((user_id).to_bytes(2, 'big'))
    time.sleep(1)
    socket.send((salon_id).to_bytes(2, 'big'))
    time.sleep(1)
    get_salon_messages(session_id, salon_id)

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

'''
