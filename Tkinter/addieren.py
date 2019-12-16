from tkinter import*

class MyButton(Button):
    def addieren(self):
        ausgabe.delete(0, "end")
        zahl1 = int(eingabe1.get())
        zahl2 = int(eingabe2.get())
        eingabe1.delete(0, "end")
        eingabe2.delete(0, "end")
        ausgabe.insert(0, zahl1+zahl2)


fenster = Tk()

fenster.geometry("300x300")
fenster.title("Rechner")
rahmen = Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)                                       #Umrandung erstellen

label1 = Label(rahmen, text="Zahl 1:")
label1.grid(row=1, column=1, padx=30, pady=30)                           #pady oder padx gelten für alle kommenden grid layouts
eingabe1 = Entry(rahmen, bd=2, width=22)
eingabe1.grid(row=1, column=2)

label2 = Label(rahmen, text="Zahl 2:")
label2.grid(row=2, column=1)
eingabe2 = Entry(rahmen, bd=2, width=22)
eingabe2.grid(row=2, column=2)

button = MyButton(rahmen, text="addieren!")
button["command"] = button.addieren
button.grid(row=3, column=2, pady=20)

ausgabe = Entry(rahmen, bd=2, width=22)
ausgabe.grid(row=4, column=2, pady=20)

fenster.mainloop()