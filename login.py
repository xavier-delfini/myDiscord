from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class Connexion:
    def __init__(self, root):
        self.root=root
        self.root.title("Connexion")
        self.root.geometry("800x600")
        self.root.config(bg="#f5f5f5")

        login_frame = Frame(self.root, bg="#FFFFFF", bd=0, highlightthickness=0)
        login_frame.pack(expand=True, padx=200, pady=100)

        title = Label(login_frame, text="Connexion", font=("Arial",40), bg="#FFFFFF", fg="#333333")
        title.grid(column=0, row=0, columnspan=2, pady=20)

        lbl_email = Label(login_frame, text="E-mail", font=("Arial", 20),bg="#FFFFFF", fg="#333333")
        lbl_email.grid(column=0, row=1, padx=10, pady=10, sticky="E")

        self.txt_email= Entry(login_frame, font=("Arial",20), bg="#f5f5f5", bd=0, highlightthickness=0)
        self.txt_email.grid(column=1, row=1, padx=10, pady=10, sticky="W")

        lbl_password = Label(login_frame, text="Mot de passe", font=("Arial", 20), bg="#FFFFFF", fg="#333333")
        lbl_password.grid(column=0, row=2, padx=10, pady=10, sticky="E")

        self.txt_password = Entry(login_frame, font=("Arial", 20), bg="#f5f5f5", show="*", bd=0, highlightthickness=0)
        self.txt_password.grid(column=1, row=2, padx=10, pady=10, sticky="W")

        login_btn = Button(login_frame, text="Se connecter", cursor="hand2",command=self.connexion, font=("Arial", 15), bd=0, bg="#333333",fg="#FFFFFF", pady=10, padx=20,)
        login_btn.grid(column=0, row=3, columnspan=2, pady=20)

        creer_btn= Button(login_frame, text="Créer un nouveau compte", cursor="hand2",command=self.fenetre_creer, font=("Arial",15),bd=0, bg="#FFFFFF", fg="#333333", pady=10)
        creer_btn.grid(column=0, row=4, padx=10, pady=20, sticky="E")




    def connexion(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Erreur", "Veillez saisir l'Email et le mot de passe", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="test", database="discord")
                cur = con.cursor()  # Ajout de cette ligne
                cur.execute("SELECT * FROM utilisateurs WHERE email=%s AND motdepasse=%s",(self.txt_email.get(), self.txt_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showwarning("Erreur", "Invalide email ou password",parent=self.root)
                else:
                    messagebox.showinfo("Réussite", "vous allez être redirigé")
                    con.close()

            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexione{str(ex)}", parent=self.root)

    def fenetre_creer(self):
        self.root.destroy()
        import formulaire


root=Tk()
obj = Connexion(root)
root.mainloop()
