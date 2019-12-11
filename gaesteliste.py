"""
Aufgabe Gästeliste
"""
f = open("dateien/gaeste.txt", "a")

# while True:
#     name = input("Bitte geben Sie einen Namen ein. quit zum abbrechen: ")
#     if name == "quit":
#         break
#     f.write(name +"\n")

"""
mit Abfrage
"""

a = True
while a == True:
    try:
        anzahl = eval(input("Wie viele Personen wollen Sie hinzufügen?:"))

        for i in range(anzahl):
            name = input("Bitte name eingeben:")
            f.write(name + "\n")

        a = False

    except NameError:
        print("Sie müssen eine Zahl eingeben!")
