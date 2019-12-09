"""
r       Datei wird nur zum Lesen geöffnet
w       Datei wird nur zum Schreiben geöffnet.
        Eine bereits bestehende Datei mit diesem Namen wird überschrieben.
a       Das Programm hängt die neuen Eingaben an eine bestehende Datei an.
r+      Die Datei wird zum Lesen und zum Schreiben geöffnet.
"""
f = open("dateien/sortiment.txt", "r")
inhalt = f.readlines()
print (len(inhalt))
print(inhalt)

f = open("dateien/sortiment.txt", "a")

# marke = input("Geben Sie eine Marke ein: ")
# modell = input("Geben Sie ein Modell ein: ")
# baujahr = input("Geben Sie ein Baujahr ein: ")
# preis = input("Geben Sie einen Preis ein: ")
#
# f.write(marke+"\n")
# f.write(modell+"\n")
# f.write(baujahr+"\n")
# f.write(preis+"\n")
