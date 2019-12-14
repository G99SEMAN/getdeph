from tkinter import *

fenster = Tk()
fenster.geometry("300x100")
fenster.title("Python Kurs")
label = Label(text="Hallo Welt!")
rahmen = Frame(fenster, relief="ridge", borderwidth=3)
rahmen.pack(fill="both", expand=1)
label = Label(rahmen, text="Wilkommenzum Python Kurs!")
label.pack(expand=1)





fenster.mainloop()