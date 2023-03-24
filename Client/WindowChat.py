from tkinter import *
from Database import Database
import mysql.connector


class WindowChat(Database):
    def __init__(self):
        super().__init__()
        master = Tk()
        master.title("MyDiscord")
        master.geometry("800x600")
        master.resizable(False, False)
        master.configure(background="#4f4d4d")
        self.curseur = self.db().cursor()
        #TODO:Passer par le serveur
        self.curseur.execute("SELECT nom FROM salon")
        self.result = self.curseur.fetchall()
        self.result = [nom[0].replace("{", "") for nom in self.result]

        self.selected1 = StringVar()

        self.option_menu = OptionMenu(master, self.selected1, *self.result)
        self.option_menu.config(width=30, bg='#a09797', fg='#000000', font=('Arial', 16))
        self.option_menu.pack()

        self.psd = Entry(master, width=50, bg='#a09797', fg='#000000', font=('Arial', 16))
        self.psd.place(x=35, y=550)

        self.btn_inscription = Button(master, text="Send", width=7, height=1, bg='#6451ef', fg='#FFFFFF', font=('arial', 15, 'bold'))
        self.btn_inscription.place(x=650, y=550)
        master.mainloop()

#gui = WindowChat()

