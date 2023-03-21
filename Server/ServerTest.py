# coding: utf-8
#Test envoie info au client
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

                # Reverse the given string from the client
                data = data[::-1]

                # Send back reversed string to the client
                client.send(data)

        # Connection closed
        client.close()


def main():
        host = ""

        # Reverse a port on the computer
        # In the case it is 2002 but it can be anything
        port = 2002
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
                start_new_thread(threaded, (c,))
        server.close()
main()

