from tkinter import *

class MyButton(Button):
    def aktion(self):
        print("Sie haben den Button gedrückt")

fenster = Tk()

fenster.geometry("300x100")
fenster.title("Python Kurs")
rahmen = Frame(fenster, relief="ridge", borderwidth=3)
rahmen.pack(fill="both", expand=1)

button = Button(rahmen, text="OK", command=fenster.destroy)
button.pack(side="bottom")
button2 = MyButton(rahmen, text="Action!")
button2["command"] = button2.aktion
button2.pack(side="bottom")

label = Label(rahmen, text="Wilkommenzum Python Kurs!")
label.pack(expand=1)

fenster.mainloop()