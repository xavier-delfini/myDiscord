import concurrent.futures
import socket
from NoSession import NoSession

def instance_create(c):

    instance_object = NoSession(c)
    print("Lancement no session")
    instance_object.Main()
    del instance_object
    concurrent.futures.Future.done()
def main():
    host = ""
    port = 15555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print("Le serveur à démarrer sur le port", port, "et attend des clients")
    server.listen(5)
    print("socket is listening")

    #Création d'une instance de la fonction instance_create, il permet la connexion de plusieurs hotes en simultanée

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            c, addr = server.accept()#Attente d'une connexion
            print('Connexion de :', addr[0], ':', addr[1])
            executor.submit(instance_create, c)#Création d'une instance utilisant la fonction instance_create
            #Et qui passe en argument l'objet de connexion
    server.close()
main()
