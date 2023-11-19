from tkinter import Tk, Label, Button, ttk, Spinbox, Text, StringVar, END
from functions import encrypt as functions_module

class EncryptPage(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("+500+200")
        self.resizable(False, False)
        self.title("Ceaser cipher Encrypter/Decrypter" )

    def init_page(self):
        Label(self, text="Encrypter by Caesar cipher", font=12).pack()

        frame_1 = ttk.Frame(self, padding="3 3 12 12")
        frame_1.pack()
        Label(frame_1, text="Shift: ", font=12).grid(column=0, row=0)
        self.shift = StringVar(value=1)
        self.shift_entry = Spinbox(frame_1, from_=1, to=26, width=3, font=12, textvariable=self.shift)
        self.shift_entry.grid(column=1, row=0)

        frame_2 = ttk.Frame(self, padding="3 3 12 12")
        frame_2.pack()
        Label(frame_2, text="Text: ", font=12).grid(column=0, row=0)
        self.text_entry = Text(frame_2, width=40, height=10, font=12)
        self.text_entry.grid(column=1, row=0)

        Button(self, text="Encrypt", command=lambda: self.encrypt(), font=12).pack()
        self.encrypted_text = Text(self, width=40, height=10, font=12)
        self.encrypted_text.pack()
        Button(self, text="Close", command=lambda: self.close_page(), font=12).pack()

    def encrypt(self):
        self.encrypted_text.delete('1.0' , END)
        self.encrypted_text.insert("1.0", functions_module.encrypt(self.text_entry.get("1.0", END), int(self.shift_entry.get())))
        self.copy_to_clipboard(self.encrypted_text.get("1.0", END))

    def close_page(self):
        self.destroy()

    def copy_to_clipboard(self, text_to_copy):
        self.clipboard_clear()
        self.clipboard_append(text_to_copy)

if __name__ == "__main__":
    APP_ABOUT = EncryptPage()
    APP_ABOUT.mainloop()