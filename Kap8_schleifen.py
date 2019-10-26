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


#
# liste = [12, 18, 3, 6, 0, 46, 234, 23]
#
# wert = eval(input("Welcher wert soll dividiert werden?"))
# for n in liste:
#     print(n)
#     if n == 0:
#         print("Fehler Zahlen dürfen nicht durch 0 geteilt werden")
#         continue
#     print(wert/n)

#####aufgabe1
#
# for i in range(1, 10):
#     print("QW von", i, "=", i*i)
# n=1
# while n <=10:
#     print("QW von", n, "=", n*n)
#     n+=1

#####aufgabe 2
# staedte=['köln', "frankfurt", "kassel", "bechen", "frechen", "hamburg", "trier", "mainz", "dortmund", "münchen"]
# print(len(staedte))
# for i in staedte:
#     print(i)
#
# n=0
# while n<len(staedte):
#     print(staedte[n])
#     n+=1


######Aufgabe 3


while True:
    zahl = eval(input("Geben Sie eine Zahl ein welche verdoppelt werden soll: "))
    print(zahl*2)
    ja = input("wollen sie nochmal? ja/nein")
    if ja != "ja":
        break
print("ENDE!")
