from tkinter import *
from tkinter import messagebox
from Client.Classes.ClientCommands import ClientCommands
#TODO:Améliorer le front
class Form:
    def __init__(self):
        self.root = Tk()
        self.root.title("Formulaire")
        self.root.geometry("1920x1080+0+0")

        frame1 = Frame(self.root, bg="lightgrey")
        frame1.place(x=500, y=200, width=700, height=500)

        title = Label(frame1, text="Créer un compte", font=("arial", 20, "bold"), bg="lightgrey", fg="black")
        title.place(x=50, y=30)

        aff_prenom = Label(frame1, text="prénom", font=("arial", 20, "bold"), bg="lightgrey", fg="black")
        aff_prenom.place(x=50, y=100)
        self.ecri_prenom = Entry(frame1, font=("arial",), bg="lightgrey")
        self.ecri_prenom.place(x=50, y=130)

        aff_nom = Label(frame1, text="nom", font=("arial", 20, "bold"), bg="lightgrey", fg="black")
        aff_nom.place(x=370, y=100)
        self.ecri_nom = Entry(frame1, font=("arial",), bg="lightgrey")
        self.ecri_nom.place(x=370, y=130)

        aff_email = Label(frame1, text="email", font=("arial", 20, "bold"), bg="lightgrey", fg="black")
        aff_email.place(x=50, y=160)
        self.ecri_email = Entry(frame1, font=("arial",), bg="lightgrey")
        self.ecri_email.place(x=50, y=190)

        aff_mdp = Label(frame1, text="mdp", font=("arial", 20, "bold"), bg="lightgrey", fg="black")
        aff_mdp.place(x=370, y=160)
        self.ecri_mdp = Entry(frame1, show="*", font=("arial",), bg="lightgrey")
        self.ecri_mdp.place(x=370, y=190)

        aff_confmdp = Label(frame1, text="Confirme le mdp", font=("arial", 20, "bold"), bg="lightgrey", fg="black")
        aff_confmdp.place(x=50, y=240)
        self.ecri_confmdp = Entry(frame1, show="*", font=("arial",), bg="lightgrey")
        self.ecri_confmdp.place(x=50, y=270)

        btn = Button(frame1, text="créer", cursor="hand2", command=self.create_new_user, font=("arial", 15,), bg="cyan",
                     fg="black")
        btn.place(x=250, y=430)
        btn2 = Button(frame1, text="connexion", cursor="hand2", command=self.create_login_window, font=("arial", 15,),
                      bg="cyan", fg="black")
        btn2.place(x=550, y=250)
        self.root.mainloop()

    def create_new_user(self):
        if self.ecri_prenom.get() == "" or self.ecri_email.get() == "" or self.ecri_nom.get() == "" or self.ecri_mdp.get() == "" or self.ecri_confmdp.get() == "":
            messagebox.showerror("Erreur",
                                 "à quoi tu joues ? tu veux que jte ban ip fdp ? Allez hop hop faut tout remplir sans se tromper",
                                 parent=self.root)
        elif " " in self.ecri_prenom.get() or " " in self.ecri_nom.get():
            messagebox.showerror("Erreur", "Pas d'espace ou autre caracter pour les nom ou prénom juste -",
                                 parent=self.root)

        elif self.ecri_mdp.get() != self.ecri_confmdp.get():
            messagebox.showerror("Erreur",
                                 "Euuuuh je crois tu t'es trompé mec surement 123 et 132 ça arrive de confondre les deux quand ton qi est negatif",
                                 parent=self.root)
        else:
            print("début CREATE_new_USER")
            Command = ClientCommands()
            if Command.user_creation(self.ecri_prenom.get(), self.ecri_nom.get(), self.ecri_email.get(), self.ecri_mdp.get()) == 1:
                messagebox.showinfo("Success", "Votre compte a été crée", parent=self.root)
            else:
                messagebox.showerror("Erreur", "Ce mail existe déjà", parent=self.root)
    def create_login_window(self):
        self.root.destroy()
        from Client.Classes.Login import Login
        obj = Login()
