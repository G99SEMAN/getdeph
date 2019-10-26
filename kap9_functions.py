# def begruessung(name, zahl=0):
#     print("Hallo", name)
#     print("zahl=", zahl)
#
# name=input("Wie ist dein Name? : ")
# zahl= eval(input("Nennen Sie eine Zahl :"))
# begruessung(name, zahl)












# def personendaten (name="unbekannt", wohnort= "unbekannt", alter="unbekannt"):
#     print("Name: ", name)
#     print("Wohnort: ", wohnort)
#     print("Alter: ", alter)
#     print("\n")
#
# personendaten()
# personendaten("Kevin", "Köln", 31)









# def formel (x):
#     wert= 2*x*x+4*x+9
#     wert2= 3*x*x+2*x-7
#     return [wert, wert2]    #list
#     #return wert, wert2     #tupel
#
#
#
# ergebnisse= formel(4)
# print(type(ergebnisse))
# print(ergebnisse[0])
# print(ergebnisse[1])







import functions
# formel = functions.formel           ##wenn mann den Pfad einmal eingegeben hat muss  man ihn nicht immer vor die Funktion schreiben siehe unten
# eingabe = eval(input("Bitte eine Zahl eingeben: "))
# #print(functions.formel(eingabe))
# print(formel(eingabe))





#######Aufgabe 1
schritte = functions.zweierschritte

z1 = eval(input("Zahl1: "))
z2 = eval(input("Zahl2: "))
schritte(z1, z2)
