# coding: utf-8
import hashlib
import socket
import pickle
import time
import pyaudio
from Client.parameters import constant as c
import wave

# Importation des constantes SERVER_IP et SERVER_PORT(déclarer comme constantes puisque ces valeurs ne sont pas censer changer en cours d'execution dans notre cas)

#Fichier de test dans Test.ClientTest
#TODO:Voice Chat envoie , Voice Chat reception
class ClientCommands:
    def __init__(self):
        self.__session_id = -1
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((c.SERVER_IP, c.SERVER_PORT))
        print("Connection on {}".format(c.SERVER_PORT))

    def get_session_id(self):
        self.__session_id = int.from_bytes(self.__socket.recv(1024), byteorder='big')
        print(self.__session_id)

    def authentification_with_server(self):
        # Envoi de l'id de session a chaque commande afin d'authentifier la requête
        session_id = self.__session_id.to_bytes(2, 'big')
        self.__socket.send(session_id)
        time.sleep(1)

    def get_salon_messages(self, salon_name):
        self.authentification_with_server()
        # Envoi de la commande GetMessage
        print("Envoie commande getmessage")
        self.__socket.send(bytes("GetMessage", "utf-8"))
        #time.sleep(1)
        # Envoie identifiant salon
        print("Envoie nom du salon")
        salon_name = bytes(salon_name, "utf-8")
        print(salon_name)
        self.__socket.send(salon_name)
        #time.sleep(1)
        # Reception données messages
        Data = self.__socket.recv(10024)
        print(Data)
        receved_string = pickle.loads(Data)
        print(list(receved_string))
        return receved_string

    def send_message(self,message, salon_id):
        self.authentification_with_server()
        print("Envoie commande envoye message")
        self.__socket.send(bytes("SendMessage", "utf-8"))
        #time.sleep(1)
        data = pickle.dumps([message,salon_id])
        print("Envoie du message")
        self.__socket.send(data)
        #time.sleep(1)

    def disconnect(self, session_id):
        if session_id is not None:
            self.authentification_with_server()
            self.__socket.send(bytes("Disconnect", "utf-8"))
            time.sleep(1)

    def user_connexion(self, mail, password):
        password = self.__hash_password(password)
        print("Envoie requete")
        self.__socket.send(bytes("connexion", "utf-8"))
        time.sleep(1)
        print("Envoie infos")
        self.__socket.send(pickle.dumps((mail, password)))
        print("Attente reception infos")
        connexion_response = self.__socket.recv(512)
        print("Données recu :", connexion_response)
        if connexion_response == b'Sucessed':
            self.get_session_id()
            return 1
        else:
            return 0

    def user_creation(self, prenom, nom, mail, password):
        password=self.__hash_password(password)
        user_infos = pickle.dumps((prenom, nom, mail, password))
        self.__socket.send(bytes("user_create", "utf-8"))
        time.sleep(1)
        self.__socket.send(user_infos)
        result = self.__socket.recv(512)

        print(result)
        if result == b'Account Created':
            return 1
        elif result == b'Failed':
            return 2

    def __hash_password(self,password):
        hash_object = hashlib.sha256()
        hash_object.update(password.encode())
        hex_hash = hash_object.hexdigest()
        return hex_hash

    def getSalonList(self):
        self.authentification_with_server()
        self.__socket.send(bytes("GetSalonList", "utf-8"))
        received_data = self.__socket.recv(1024)
        received_data = pickle.loads(received_data)
        print(received_data)
        return received_data

    def SearchPrivateSalon(self, passcode):
        self.authentification_with_server()
        self.__socket.send(bytes("SearchPrivateSalon", "utf-8"))
        time.sleep(1)
        self.__socket.send(bytes(passcode, "utf-8"))
        print("Reception résultat recherche salon")
        salon = self.__socket.recv(1024)
        salon = pickle.loads(salon)
        return salon

    def CreateSalon(self, name, accessibility=0, passcode=None):
        self.authentification_with_server()
        self.__socket.send(bytes("CreateSalon", "utf-8"))
        time.sleep(1)
        data = pickle.dumps([name, accessibility, passcode])
        self.__socket.send(data)
        result = self.__socket.recv(512)
        if result == b'Ok':
            return 1
        else:
            return 2

    '''def VoiceChat(self,salon):

        audio= pyaudio.PyAudio()
        buffer=1024
        output_stream = audio.open(format=pyaudio.paInt16,output=True, rate=44100, channels=2,frames_per_buffer=buffer)
        input_stream = audio.open(format=pyaudio.paInt16,input=True, rate=44100, channels=2,frames_per_buffer=buffer)
    def record(self):
        while True:
            data = self.input_stream.read(self.buffer)
            self.transport.write(data, self.another_client)'''


