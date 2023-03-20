# coding: utf-8

import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))
string = "Test"
if len(string) <= 1000:  # Limite de caractères imposé par le paquet que l'on envoie
    bytesconvert = bytes(string, "utf-8")
    socket.send(bytesconvert)
else:
    print("Erreur: votre message ne doit pas dépasser les 1000 caractères")

print(string)
socket.close()
