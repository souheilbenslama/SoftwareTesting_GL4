import base64
import hashlib
import tkinter as tk

class DecodePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(bg="black")

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=5)

        # Login
        menuText = tk.Label(self, text="Decode")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=3, row=0)

        # username
        tk.Label(self, text="Message :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=1, column=0)

        T = tk.Text(self, height=5, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                    insertbackground="#57B947")
        T.grid(row=1, column=1)

        output_text = tk.Label(self, text="Output :", bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output_text.grid(row=3, column=0)
        output = tk.Text(self, height=2, width=52, relief='flat', bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output.grid(row=3, column=1)

        # Coding button
        menu1_text = tk.StringVar()
        menu1_btn = tk.Button(self, command=lambda: self.getdecode(T, output, output_text, "64"), textvariable=menu1_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=10)
        menu1_text.set("Base 64")
        menu1_btn.grid(column=0, row=2)

        # Decoding button
        menu2_text = tk.StringVar()
        menu2_btn = tk.Button(self, command=lambda: self.getdecode(T, output, output_text, "32"), textvariable=menu2_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=10)
        menu2_text.set("Base 32")
        menu2_btn.grid(column=1, row=2)

        # Decoding button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: self.getdecode(T, output, output_text, "16"), textvariable=menu3_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=10)
        menu3_text.set("Base 16")
        menu3_btn.grid(column=2, row=2)

        # Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda: controller.show_frame(3), textvariable=quit_text,
                             font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=3, row=4)

    def getdecode(self, input, out, out_text, type):
        message = input.get("1.0", "end-1c")

        try:
            out.delete(1.0, "end")
            out.insert(1.0, decode(message,type))
        except Exception as e:
            print(e)
            out.delete(1.0, "end")
            out.insert(1.0,"Invalid Base of text")

def decode( input, type) :
    if (type == "64"):
        return base64.b64decode(input.encode('ascii')).decode('ascii')

    if (type == "16"):
        return base64.b16decode(input.encode('ascii')).decode('ascii')

    if (type == "32"):
        return base64.b32decode(input.encode('ascii')).decode('ascii')

