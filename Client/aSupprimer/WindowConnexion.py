from tkinter import *

#TODO:Fichier a supprimer/utiliser pour la connexion
class WindowConnexion:
    def __init__(self, master):
        self.master = master
        master.title("MyDiscord")
        master.geometry("800x600")
        master.resizable(False, False)
        master.configure(background="#4f4d4d")

        self.echo = Label(master, text="MyDiscord", width=24, bg='#4f4d4d', fg='#bfbdbd', height=2, font=('arial', 30,))
        self.echo.place(x=90, y=100)

        self.mail = Entry(master, width=50, bg='#a09797', fg='#000000', font=('Arial', 16, 'bold'))
        self.mail.pack()
        self.mail.place(x=90, y=200)

        self.pswd = Entry(master, width=50, bg='#a09797', fg='#000000', font=('Arial', 16))
        self.pswd.pack()
        self.pswd.place(x=90, y=300)

        self.btn_connexion = Button(master, text="Connexion", width=13, height=1, bg='#6451ef', fg='#FFFFFF', font=('arial', 15, 'bold'))
        self.btn_connexion.place(x=300, y=400)

        self.btn_inscription = Button(master, text="Inscription", width=13, height=1, bg='#6451ef', fg='#FFFFFF', font=('arial', 15, 'bold'))
        self.btn_inscription.place(x=300, y=450)



root = Tk()
gui = WindowConnexion(root)
root.mainloop()
