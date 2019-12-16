from tkinter import*

class Addition:
    def addieren(self):
        zahl1=int(eingabe1.get())
        zahl2=int(eingabe2.get())


fenster = Tk()
fenster.geometry("300x300")
fenster.title("Rechner")
rahmen = Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)

label1 = Label(rahmen, text="Zahl 1:")
label1.grid(row=1, column=1, padx=30)                           #pady oder padx gelten für alle kommenden grid layouts
eingabe1 = Entry(rahmen, bd=2, width=22)
eingabe1.grid(row=1, column=2)

label2 = Label(rahmen, text="Zahl 2:")
label2.grid(row=2, column=1)
eingabe2 = Entry(rahmen, bd=2, width=22)
eingabe2.grid(row=2, column=2)





fenster.mainloop()