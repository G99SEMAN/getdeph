from tkinter import *


class Hinzufuegen(Button):
    def hinzufuegen(self):
        class MyButton(Button):
            def aktion1(self):
                f = open("sortiment.txt", "a")
                inhalt = eingabe1.get()
                f.write(inhalt + "\n")

                inhalt = eingabe2.get()
                f.write(inhalt + "\n")

                inhalt = eingabe3.get()
                f.write(inhalt + "\n")

                inhalt = eingabe4.get()
                f.write(inhalt + "\n")

                inhalt = eingabe5.get()
                f.write(inhalt + "\n")

                f.write("\n")

                f.close()

                fenster.destroy()

        fenster = Tk()
        fenster.geometry("550x400")
        fenster.title("Fahrzeug hinzufügen")
        rahmen = Frame(fenster, relief="ridge", borderwidth=5)
        rahmen.pack(fill="both", expand=1)

        labelHaupt = Label(rahmen, text="Geben Sie die Daten des " + "neuen Fahrzeugs ein:")
        labelHaupt.config(font=("Arial", 14, "bold"))
        labelHaupt.place(x=50, y=10)

        label1 = Label(rahmen, text="Artikelnummer:")
        label1.place(x=100, y=100)
        eingabe1 = Entry(rahmen, bd=2, width=22)
        eingabe1.place(x=200, y=100)

        label2 = Label(rahmen, text="Marke:")
        label2.place(x=100, y=140)
        eingabe2 = Entry(rahmen, bd=2, width=22)
        eingabe2.place(x=200, y=140)

        label3 = Label(rahmen, text="Model:")
        label3.place(x=100, y=180)
        eingabe3 = Entry(rahmen, bd=2, width=22)
        eingabe3.place(x=200, y=180)

        label4 = Label(rahmen, text="Baujahr:")
        label4.place(x=100, y=220)
        eingabe4 = Entry(rahmen, bd=2, width=22)
        eingabe4.place(x=200, y=220)

        label5 = Label(rahmen, text="Preis:")
        label5.place(x=100, y=260)
        eingabe5 = Entry(rahmen, bd=2, width=22)
        eingabe5.place(x=200, y=260)

        button = MyButton(rahmen, text="Eingabe")
        button["command"] = button.aktion1
        button.place(x=180, y=320)

        fenster.mainloop()
