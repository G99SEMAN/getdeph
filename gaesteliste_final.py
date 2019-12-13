

while True:
    f = open("dateien\gaeste.txt", "r")
    liste = f.readlines()
    f.close()
    """MAIN"""

    print("Liste V1.0")
    print("(1) Liste anzeigen")
    print("(2) Liste hinzufügen")
    print("(3) Liste löschen")
    print("(4) ENDE")
    option = eval(input("Option: "))

    if option == 1:
        for i in range(len(liste)):
            print(liste[i])
    elif option == 2:
        f = open("dateien\gaeste.txt", "a")
        eingabe = input("wen wolllen Sie hinzufügen?: ")
        f.write(eingabe + "\n")
    elif option == 3:
        geloescht = False
        eingabe = input("Wen möchten Sie löschen?: ")

        for i in range(len(liste)):
            if liste[i] == eingabe + "\n":
                f = open("dateien\gaeste.txt", "w")
                liste = liste[:i] + liste[i + 1:]
                for linie in liste:
                    f.write(linie)
                print(eingabe, "wurde erfolgreich gelöscht.")
                geloescht = True
                break
        if not geloescht:
            print(eingabe, "ist nicht in der Liste enthalten.")
    elif option == 4:
        break
    else:
        print("falsche eingabe")