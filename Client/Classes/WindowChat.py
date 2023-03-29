from tkinter import *
from tkinter import ttk
from Client.Classes.ClientCommands import ClientCommands
from functools import partial


# TODO:Affichage messages
# TODO:Changement salons
# TODO:Création salons


class WindowChat:
    def __init__(self, connexion):
        self.connexion = connexion
        self.current_salon = 1
        master = Tk()
        master.title("MyDiscord")
        master.geometry("800x600")
        master.resizable(False, False)
        master.configure(background="#4f4d4d")
        self.result = [nom[1].replace("{", "") for nom in self.connexion.getSalonList()]

       

        self.selected1 = StringVar()

        self.option_menu = OptionMenu(master, self.selected1, *self.result)
        self.option_menu.config(width=30, bg='#a09797', fg='#000000', font=('Arial', 16))
        self.option_menu.pack()

        self.btn_newchan = Button(master, text="New Chanel", width=10, height=1, bg='#6451ef', fg='#FFFFFF',
                                  font=('arial', 15, 'bold'), command=self.open_window)
        self.btn_newchan.place(x=605, y=0)

        self.mes_var = StringVar()

        self.psd = Entry(master, width=50, textvariable=self.mes_var, bg='#a09797', fg='#000000', font=('Arial', 16))
        self.psd.place(x=35, y=550)

        self.btn_inscription = Button(master, text="Send", height=1, bg='#6451ef', fg='#FFFFFF',
                                      font=('arial', 15, 'bold'), command=partial(self.send_message),
                                      width=7)
        self.btn_inscription.place(x=650, y=550)
        master.mainloop()

    def send_message(self):

        if self.psd.get() != "":
            self.connexion.send_message(self.psd.get(), self.current_salon)
            self.mes_var.set("")
        # Commande actualisation pour la récupération des messages changer

    def open_window(self):  # fonction pour ouvrir une fenètre secondaire
        window = Toplevel()
        window.title("Sous-fenêtre")
        window.geometry("200x200")
        window.configure(background="#4f4d4d")
        entryun = Entry(window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16),
                        bd=5)  # notre entrée pour marquer la somme
        entryun.pack()
        entrydeu = Entry(window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16),
                         bd=5)  # notre entrée pour marquer la somme
        entrydeu.pack()
        entrytroi = Entry(window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16),
                          bd=5)  # notre entrée pour marquer la somme
        entrytroi.pack()
        c1 = Checkbutton(window, text='Python', onvalue=1, offvalue=0)
        c1.pack()
        Button(window, text="add", width=5, height=1, font=('arial', 30, 'bold'), ).place(x=25, y=100)
# command=lambda:self.command.CreateSalon(entryun,entrydeu,entrytroi)
