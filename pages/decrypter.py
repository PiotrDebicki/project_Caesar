from tkinter import Tk, Label, Button, ttk, Text, END
from functions import decrypt as functions_module

class DecryptPage(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("+500+200")
        self.resizable(False, False)
        self.title("Ceaser cipher Encrypter/Decrypter" )

    def init_page(self):
        Label(self, text="Encrypter by Caesar cipher", font=12).pack()
        
        frame_1 = ttk.Frame(self, padding="3 3 12 12")
        frame_1.pack()
        Label(frame_1, text="Text: ", font=12).grid(column=0, row=0)
        self.text_entry = Text(frame_1, width=40, height=5, font=12)
        self.text_entry.grid(column=1, row=0)

        
        Button(self, text="Decrypt", command=lambda: self.decrypt(), font=12).pack()

        self.decrypted_text = Text(self, width=40, height=10, font=12)
        self.decrypted_text.pack()

        Button(self, text="Close", command=lambda: self.close_page(), font=12).pack()


    def decrypt(self):
        self.decrypted_text.delete("1.0", END)
        self.decrypted_text.insert("1.0", functions_module.decrypt(self.text_entry.get("1.0", END)))
        self.copy_to_clipboard(self.decrypted_text.get("1.0", END))

    def copy_to_clipboard(self, text_to_copy):
        self.clipboard_clear()
        self.clipboard_append(text_to_copy)

    def close_page(self):
        self.destroy()


if __name__ == "__main__":
    APP_ABOUT = DecryptPage()
    APP_ABOUT.mainloop()