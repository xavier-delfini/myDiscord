import concurrent.futures
from Client.Classes.ClientCommands import ClientCommands

#TODO:Fixer ce fichier
def launch_spam():
    Test = ClientCommands()
    Test.user_connexion("a", "a")
    Test.send_message("Ceci est un test", 1)
    print(Test.get_salon_messages(1))
    Test.getSalonList()
i=0
with concurrent.futures.ThreadPoolExecutor() as executor:
    while i!=10:
        executor.submit(launch_spam())#Création d'une instance utilisant la fonction instance_create
        #Et qui passe en argument l'objet de connexion
        i+=1
