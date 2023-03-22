import concurrent.futures

import ClientTest as CT

def launch_spam():
    while i!=10:
        id=CT.get_session_id()
        CT.get_salon_messages(id,1)
        CT.send_message(id,1,"Salut",1)
        #socket.close()
i=0
concurrent.futures.
with concurrent.futures.ThreadPoolExecutor() as executor:
    while i!=10:
        executor.submit(launch_spam())#Création d'une instance utilisant la fonction instance_create
        #Et qui passe en argument l'objet de connexion
        i+=1
