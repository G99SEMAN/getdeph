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








def formel (x):
    if 2*x*x+4*x+9 < 50:
        return 2*x*x+4*x+9
    else:
        return 3*x*x+2*x-7

eingabe = eval(input("Bitte eine Zahl eingeben: "))
print(formel(eingabe))
