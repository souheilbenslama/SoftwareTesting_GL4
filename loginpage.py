import tkinter as tk
from PIL import ImageTk, Image

from dbconnection import DAO
from homepage import HomePage
from registerpage import RegisterPage


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="black")
        self.parent=parent

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=8)

        image = Image.open("logo.png")
        image = image.resize((200, 200), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=image1)
        label.image = image1

        label.configure(background='black')
        label.grid(columnspan=3, row=0)

        # Login
        loginText = tk.Label(self, text="Connexion")
        loginText.config(font=("Anonymous Pro", 30))
        loginText.config(fg="#FFFFFF")
        loginText.config(bg="black")
        loginText.grid(column=1, row=1)

        # username
        tk.Label(self, text="User Name :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=2, column=1)
        username = tk.StringVar()
        tk.Entry(self, textvariable=username, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                 insertbackground="#57B947").grid(row=3, column=1)

        # password label and password entry box
        tk.Label(self, text="Password :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=4, column=1)
        password = tk.StringVar()
        tk.Entry(self, textvariable=password, show='*', font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                 insertbackground="#57B947").grid(row=5, column=1)

        # button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda: self.login(username, password, controller),
                                  textvariable=connexion_text, font=("Anonymous Pro", 14), bg="#57B947", fg="black")
        connexion_text.set("Login")
        connexion_btn.grid(column=1, row=6)

        # button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda: self.register(controller), textvariable=connexion_text,
                                  font=("Anonymous Pro", 14), bg="#57B947", fg="black")
        connexion_text.set("Register")
        connexion_btn.grid(column=1, row=7)

    def login(self, email, password, controller):
        print("email entered :", email.get())
        print("password entered :", password.get())
        dao = DAO()
        #result = dao.login(email.get(), password.get())
        #if (result):
        #    print("hello")

        controller.show_frame(2)

    def register(self, controller):
        controller.show_frame(1)

