from tkinter import Tk, Label, Button

class AboutPage(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.eval('tk::PlaceWindow . center')
        self.resizable(False, False)
        self.title("Ceaser cipher Encrypter/Decrypter" )
        self.app_name = "Ceaser cipher Encrypter/Decrypter" 
        self.app_version = "0.1.1"
        self.app_url = "https://github.com/PiotrDebicki/project_Caesar"
        self.app_ = "Copyright © 2018 Piotr Debicki.\nAll rights reserved."

    def init_page(self):
        Label(self, text=self.app_name).pack()
        Label(self, text=self.app_version).pack()
        Label(self, text=self.app_url).pack()
        Label(self, text=self.app_).pack()
        Button(self, text="Close", command=lambda: self.destroy()).pack()

if __name__ == "__main__":
    APP_ABOUT = AboutPage()
    APP_ABOUT.mainloop()