import socket
import pickle

hote = "localhost"
port = 2002
# Test envoie de paquet limité a 64 caractères
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))
endingmessage = "End Of Transmission"
string = "b"

bytesconvert = bytes(string, "utf-8")
socket.send(bytesconvert)
Data = []
recepted = socket.recv(2048)

#recepted_string = pickle.loads(recepted)
print(recepted_string)