from tkinter import Tk, Label, Button, ttk, StringVar, IntVar, Spinbox, Entry, Text

class EncryptPage(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.eval('tk::PlaceWindow . center')
        self.resizable(False, False)
        self.title("Ceaser cipher Encrypter/Decrypter" )

    def init_page(self):
        Label(self, text="Encrypter by Caesar cipher").pack()

        frame_1 = ttk.Frame(self, padding="3 3 12 12")
        frame_1.pack()
        Label(frame_1, text="Shift: ").grid(column=0, row=0)
        shift = IntVar()
        shift_entry = Spinbox(frame_1, from_=1, to=27,width=3, textvariable=shift)
        shift_entry.grid(column=1, row=0)

        frame_2 = ttk.Frame(self, padding="3 3 12 12")
        frame_2.pack()
        Label(frame_2, text="Text: ").grid(column=0, row=0)
        text = StringVar()
        text_entry = Text(frame_2, width=40, height=10)
        text_entry.grid(column=1, row=0)

        Button(self, text="Close", command=lambda: self.close_page()).pack()

    def close_page(self):
        self.destroy()

if __name__ == "__main__":
    APP_ABOUT = EncryptPage()
    APP_ABOUT.mainloop()