# a = input("Bitte geben Sie das Wort Hallo ein! ")
# print("Sie haben das Wort", a, "eingegeben")
#
# if a == "Hallo":
#     print("Sie haben das richtige Wort eingegeben")
# else:
#     print("Sie haben das falsche Wort eingegeben eingegeben!")


# a = eval(input("Bitte geben Sie die Zahl 5 ein: "))
# b = eval(input("Bitte geben Sie die Zahl 10 ein: "))
#
# if (a == 5 or b == 10):
#     print("Richtig!")
# else:
#     print("Die Eingabe war falsch!")


# bestand = eval(input("Bitte geben Sie den aktuellen Lagerbestand ein: "))
#
# if bestand >= 100:
#     print("Das Lager ist voll")
# elif bestand >= 10:
#     print(" Der Lagerbestand liegt bei", bestand, "Artikeln!")
# elif bestand > 0:
#     print("nur noch", bestand, "Artikel, bitte nachbestellen!")
# elif bestand == 0:
#     print("Lager ist leer!")
# else:
#     print("falsche Eingabe!!!")

###########Aufgabe_

dict_car1 = {"marke": "Audi", "model": "A3", "preis": 9000, "km": 198000}
dict_car2 = {"marke": "BMW", "model": "335i", "preis": 43000, "km": 23000}
dict_car3 = {"marke": "KIA", "model": "Vito", "preis": 1890, "km": 133000}
print(type(dict_car1["preis"]))
max_preis = eval(input("Bitte geben Sie ihr maximales Budget ein: "))
# i = 0
 for i in Dict_cars:
#     if max_preis > Dict_cars[i]["preis"]:
#         print(Dict_cars[i]["marke"], Dict_cars[i]["model"], "ist im Budget!")
#     else:
#         print(Dict_cars[i]["marke"], Dict_cars[i]["model"], "ist NICHT im Budget!")

if max_preis >= (dict_car1["preis"]):
    print(dict_car1["marke"])
    print(dict_car1["model"])
    print(dict_car1["preis"])
    print(dict_car1["km"])
    print("\n")

if max_preis >= dict_car2["preis"]:
    print(dict_car2["marke"])
    print(dict_car2["model"])
    print(dict_car2["preis"])
    print(dict_car2["km"])
    print("\n")

if max_preis >= dict_car3["preis"]:
    print(dict_car3["marke"])
    print(dict_car3["model"])
    print(dict_car3["preis"])
    print(dict_car3["km"])
    print("\n")
else:
   print("Leider nicht genug Geld!")
