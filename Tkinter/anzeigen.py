from tkinter import *

class Anzeigen(Button):
    def anzeigen(self):
        fenster = Tk()
        fenster.geometry("500x400")
        fenster.title("Sortiment anzeigen")
        rahmen = Frame(fenster, relief="ridge", borderwidth=5)
        rahmen.pack(fill="both", expand=1)

        label = Label(rahmen, text="Das aktuelle Sortiment:")
        label.config(font=("Arial", 14, "bold"))
        label.pack(pady=20)

        rahmen2 = Frame(rahmen, relief="ridge", borderwidth=1)
        rahmen2.pack(pady=20, padx=30)

        f = open("dateien\sortiment.txt", "r")

        inhalt = f.readlines()
        scrollbar = Scrollbar(rahmen2)

        liste = Listbox(rahmen2, yscrollcommand=scrollbar.set, width=50)
        i = 0
        for zeile in inhalt:
            if i == 0:
                ausgabe = "Artikelnummer: "+zeile
                i += 1
            elif i == 1:
                ausgabe = "Marke: "+zeile
                i += 1
