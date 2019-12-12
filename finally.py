class Obj:
    wert = 4

try:
    objekt = Obj()
    x = int(input("Wert: "))
    print("Ergebnis: ", Obj.wert/x)
except ZeroDivisionError:
    print("Es ist nicht möglich den Wert durch 0 zu teilen!")
else:
    print("Das Ergebnis wurde erfolgreich berechnet")
finally:
    del objekt
    print("Objekt gelöscht")
print("Auf Wiedersehen!")
print("Hello World")