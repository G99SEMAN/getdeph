from tkinter import*

class MyButton(Button):
    def addieren(self):
        ausgabe.delete(0, "end")
        zahl1 = int(eingabe1.get())
        zahl2 = int(eingabe2.get())
        eingabe1.delete(0, "end")
        eingabe2.delete(0, "end")
        ausgabe.insert(0, zahl1+zahl2)

class MyButton2(Button):
    def aktion(self):
        if var.get() == 1:
            fenster2 = Tk()
            fenster2.geometry("200x200")
            fenster2.title("Hinweis")
            label=Label(fenster2, text="Checkbox ist ausgewählt!")
            label.pack(fill="both", expand=1)
    def aktion2(self):
        print(var.get())


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

var = IntVar()
checkbutton = Checkbutton(rahmen, text="Bestätigen", variable=var)
checkbutton.grid(row=5, column=1)
button2 = MyButton2(rahmen, text="Eingabe")
button2["command"] = button2.aktion
button2.grid(row=5, column=2)

fenster.mainloop()