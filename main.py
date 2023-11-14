import tkinter as tk
from tkinter import Tk
from tkinter.ttk import Frame
from pages import about, encrypter

class InitWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        #method which set left-upper corner in the center of the screen 
        self.eval('tk::PlaceWindow . center')
        
        #setting the title of the window
        self.title("Ceaser cipher Encrypter/Decrypter")

        #setting the geometry of the window, resizing, WIDTHxHEIGTH, maxsize
        self.resizable(True, True)
        self.geometry("500x200")
        self.maxsize(1000, 400)

        #creating frame to set padding
        mainframe = Frame(self, padding="12 12 12 12")
        mainframe.pack()

        #adding elements to frame
        tk.Button(mainframe, text="Encrypt the text", command=lambda: encrypter.EncryptPage().init_page(), width=20).pack()
        tk.Button(mainframe, text="About Project", command=lambda: about.AboutPage().init_page(), width=20).pack()
        tk.Button(mainframe, text="Close", command=lambda: self.destroy(), width=20).pack()


if __name__ == "__main__":
    APP_INIT = InitWindow()
    APP_INIT.mainloop()