from tkinter import *
from tkinter import messagebox
from ClientCommands import ClientCommands as command

class Login:
    def __init__(self):
        self.root = Tk()
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

        creer_btn= Button(login_frame, text="Créer un nouveau compte", cursor="hand2", command=self.create_form_window, font=("Arial", 15), bd=0, bg="#FFFFFF", fg="#333333", pady=10)
        creer_btn.grid(column=0, row=4, padx=10, pady=20, sticky="E")
        self.root.mainloop()



    def connexion(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Erreur", "Veillez saisir l'Email et le mot de passe", parent=self.root)
        else:
            connexion = command()
            server_response=connexion.user_connexion(self.txt_email.get(), self.txt_password.get())
            if server_response==0:
                messagebox.showwarning("Erreur", "Identifiant ou mot de passe incorrect.",parent=self.root)
            elif server_response==1:
                messagebox.showinfo("Réussite", "vous allez être redirigé")
                self.create_chat_window()
                #TODO:Lié Connexion to Session

    def create_form_window(self):
        self.root.destroy()
        from Form import Form
        obj = Form()

    def create_chat_window(self):
        self.root.destroy()
        from WindowChat import WindowChat
        obj = WindowChat()


