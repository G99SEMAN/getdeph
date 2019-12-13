f = open("dateien\gaeste.txt", "r")
liste = f.readlines()
f.close()

geloescht = False
eingabe = input("Welchen Gast möchten Sie löschen?: ")

for i in range(len(liste)):
    print(liste[i])
    if liste[i] == eingabe + "\n":
        f = open("dateien\gaeste.txt", "w")
        liste = liste[:i] + liste[i+1:]
        for linie in liste:
            f.write(linie)
        print(eingabe, "wurde erfolgreich gelöscht.")
        geloescht = True
        break
if not geloescht:
    print(eingabe, "ist nicht in der Liste enthalten.")
