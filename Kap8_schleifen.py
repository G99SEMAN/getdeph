# n = 1
# while n <1000:
#     print(n)
#     n += 1
# a = "ja"
#
# while a == "ja":
#     b=eval(input("Welche Zahl wollen Sie verdoppeln?: "))
#     print(b*2)
#     a = input("möchten sie eine weitere Aufgabe rechnen? (ja/nein)")


#liste = [1,4,5,4,45234]
#
# i = 0
#
# while i< len(liste):
#     print(liste[i])
#     i += 1
#
# for i in liste:
#     print(i)

# dict = {"marke": "VW", "model": "Golf", "preis": 12321, 'bj': 1998}
#
# for inhalt in dict:
#     print(inhalt, dict[inhalt])

# for n in range(5, 101, 5):
#     print(n)

# liste2 =[12, 18, 3, 6, 46, 234, 23]
# wert = eval(input("Welche Zahl soll gesucht werden? :"))
# for n in liste2:
#     if n == wert:
#         print("Die Zahl", wert, "wurde gefunden")
#         break
# else:
#     print("Die die Zahl", wert, "befindet sich nicht in der Liste!")



liste = [12, 18, 3, 6, 0, 46, 234, 23]

wert = eval(input("Welcher wert soll dividiert werden?"))
for n in liste:
    print(n)
    if n == 0:
        print("Fehler Zahlen dürfen nicht durch 0 geteilt werden")
        continue
    print(wert/n)
