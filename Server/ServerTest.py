# coding: utf-8

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print ("{} connected".format( address ))

        response = client.recv(1024)
        if response != "":
                from Database import Database as db
                send_message=db()
                send_message.create_item_in_database(response,1)
                print(response)



print("Close")
client.close()
#stock.close()
