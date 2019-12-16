from tkinter import *

class MyButton(Button):
    def aktion(self):
        print("Sie haben den Button gedrückt")

fenster = Tk()

fenster.geometry("300x100")
fenster.title("Python Kurs")
rahmen = Frame(fenster, relief="ridge", borderwidth=3)
rahmen.pack(fill="both", expand=1)

button = Button(rahmen, width=10, text="OK", command=fenster.destroy)
button.grid(row=2, column=2, pady=10)
button2 = MyButton(rahmen, width=10, text="Action!")
button2["command"] = button2.aktion
button2.grid(row=2, column=1)

label = Label(rahmen, text="Wilkommenzum Python Kurs!")
label.grid(row=1, column=1, columnspan=2, padx=50, pady=15)


fenster.mainloop()