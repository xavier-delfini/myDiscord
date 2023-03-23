# coding: utf-8
# Test envoie info au client
'''
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
        '''
# Import socket programming library
import socket

# Import thread module and threading library
from _thread import *
import threading

print_lock = threading.Lock()

'''
# Threaded function
def threaded(client):

    while True:
        # Data is received from the client
        data = client.recv(1001)
        if not data:
            print('No connection, Bye')

            # Releasing lock on exit
            print_lock.release()
            break
        match data:
            case "Connexion":
                data = client.recv(1001)
            case "Inscription":
                data = client.recv(1001)
            case "GetMessage":
                data = client.recv(1001)  # Récupération de l'id du salon ainsi que de l'utilisateur
                # Send back reversed string to the client
                # client.send(data)
            case "Disconnect":
                print_lock.release()
                break

    # Connection closed
    client.close()
''''''
import threading
from Session import Session
from _thread import *
import time
from multiprocessing import Process
import pickle
time_started = time.time()
import concurrent.futures
def instance_create(c):
    #(258).to_bytes(2, 'big')
    #int.from_bytes(b'\x00\x10', byteorder='big')

    instance_object = Session(c)
    #id_session=(instance_object.print_id()).to_bytes(2, 'big')
    #print("ID SESSION RETOURNER PAR L'OBJET")
    #print(id_session)
    #c.send(id_session)

    instance_object.Main_Session()
    while True:
        instance_object.print_id()
        if time.time() > time_started + X:
            return 1


def main():
    host = ""

    # Reverse a port on the computer
    # In the case it is 2002 but it can be anything
    port = 15555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print("socket bond to port", port)

    # Put the socket into listening mode
    server.listen(5)
    print("socket is listening")

    # An infinite loop until the client exits
    while True:
        # Establish connection with client
        c, addr = server.accept()

        # Lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start the new thread and return its identifier
        Thread(target=instance_create, args=(c,),).start()

    server.close()
'''
import concurrent.futures
import socket
from NoSession import NoSession


def instance_create(c):
    instance_object = NoSession(c)
    instance_object.Main()
    concurrent.futures.Future.done()


def main():
    host = ""
    port = 15555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print("Le serveur à démarrer sur le port", port, "et attend des clients")
    server.listen(5)
    print("socket is listening")

    # Création d'une instance de la fonction instance_create, il permet la connexion de plusieurs hotes en simultanée

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            c, addr = server.accept()  # Attente d'une connexion
            print('Connexion de :', addr[0], ':', addr[1])
            executor.submit(instance_create, c)  # Création d'une instance utilisant la fonction instance_create
            # Et qui passe en argument l'objet de connexion

    server.close()


main()