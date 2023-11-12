import tkinter as tk
from tkinter import Tk
from pages import about

class InitWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Ceaser cipher encoder/decoder")
        self.resizable(True, True)
        self.maxsize(1000, 400)
        tk.Button(self, text="test", command=about.AboutPage()).grid(row=0, column=0)

if __name__ == "__main__":
    APP_INIT = InitWindow()
    APP_INIT.mainloop()