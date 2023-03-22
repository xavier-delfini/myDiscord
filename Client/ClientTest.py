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

print("Réception id")
id=socket.recv(1024)
print(id)
time.sleep(1)

print("Envoie id")
socket.send(id)
time.sleep(1)

print("Envoie GetMessage")
socket.send(bytes("GetMessage","utf-8"))
time.sleep(1)

print("Envoie identifiant")
socket.send((1).to_bytes(2, 'big'))
time.sleep(1)

print("Reception données messages")
Data=socket.recv(1500)
print(Data)
time.sleep(1)

receved_string = pickle.loads(Data)
print(list(receved_string))

socket.close()