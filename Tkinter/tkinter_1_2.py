from tkinter import *

class MyButton(Button):
    def aktion1(self):
        name = eingabe.get()
        print(name)
        eingabe.delete(0, "end")
    def aktion2(self):
        print(var.get())

fenster = Tk()

fenster.geometry("300x600")
fenster.title("Python Kurs")
rahmen = Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)

label = Label(rahmen, text="Geben Sie Ihren Namen ein:")
label.pack()

eingabe = Entry(rahmen, bd=2, width=22)
eingabe.pack()

button = MyButton(rahmen, text="Eingabe")
button["command"] = button.aktion1
button.pack()

var = IntVar()
checkbutton = Checkbutton(rahmen, text="Bestätigen", variable=var)
checkbutton.pack()

button2 = MyButton(rahmen, text="Eingabe")
button2["command"] = button.aktion2
button2.pack()

scrollbar = Scrollbar(rahmen)

liste = Listbox(rahmen, yscrollcommand=scrollbar.set)
for i in range(50):
    liste.insert(END, "Zeile " + str(i))

scrollbar.config(command=liste.yview)
liste.pack(side="left")
scrollbar.pack(side="left", fill="y")

fenster.mainloop()