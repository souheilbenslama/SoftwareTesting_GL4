import base64
import tkinter as tk
import hashlib
import base64
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random


class EncDecRsa(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(bg="black")

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=5)

        menuText = tk.Label(self, text="RSA")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=3, row=0)

        # message
        tk.Label(self, text="Message :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=1, column=0)
        message = tk.Text(self, height=5, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                          insertbackground="#57B947")
        message.grid(row=1, column=1)

        output_text = tk.Label(self, text="Output :", bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output_text.grid(row=3, column=0)
        output = tk.Text(self, height=6, width=52, relief='flat', bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output.grid(row=3, column=1)



        # Decryption button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: self.decrypt(output,message.get("1.0", "end-1c")),
                                                                 textvariable=menu3_text,
                                                                 font=("Anonymous Pro", 14), bg="#57B947", fg="black",
                                                                 width=10)
        menu3_text.set("Decrypt")
        menu3_btn.grid(column=2, row=3)
        # Encryption button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: self.encrypt(output, message.get("1.0", "end-1c"),
                                                                 ),
                              textvariable=menu3_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black",
                              width=10)
        menu3_text.set("Encrypt")
        menu3_btn.grid(column=2, row=2)

        # Export button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: self.export( ),
                              textvariable=menu3_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black",
                              width=10)
        menu3_text.set("Export Keys")
        menu3_btn.grid(column=2, row=4)


        # Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda: controller.show_frame(7), textvariable=quit_text,
                             font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=3, row=4)

        # RSA key generation
        self.keyPair = RSA.generate(2048)
        self.pubKey = self.keyPair.publickey()
        print(f"Public key: \n (n={hex(self.pubKey.n)}, \n e={hex(self.pubKey.e)})")
        print(f"Private key:\n (n={hex(self.pubKey.n)}, \n d={hex(self.keyPair.d)})")


    def encrypt(self, output, message):
        encryptor = PKCS1_OAEP.new(self.pubKey)
        encrypted = encryptor.encrypt(bytes(message, 'utf-8'))
        out=binascii.hexlify(encrypted)
        output.delete("1.0", "end-1c")
        output.insert('1.0',out)
        print("Encrypted:", out)

    def decrypt(self, output, message):
        output.delete("1.0", "end-1c")
        decryptor = PKCS1_OAEP.new(self.keyPair)
        decrypted = decryptor.decrypt(binascii.unhexlify(message))
        output.insert('1.0',decrypted)

        print('Decrypted:', decrypted)
    def export(self):
        pubKeyPEM = self.pubKey.exportKey()
        print(pubKeyPEM.decode('ascii'))

        privKeyPEM = self.keyPair.exportKey()
        print(privKeyPEM.decode('ascii'))
