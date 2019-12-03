import sys


try:
    x = int(input("Bitte eine Zahl eingeben durch welche 4 geteilt werden soll:"))
    print(4/x)
except ZeroDivisionError:
    print("Du kannst nicht durch 0 teilen!")
except ValueError:
    print("Du musst ein int eingeben!")
except:
    print("Folgender Fehler ist aufgetreten:", sys.exc_info()[0])               #gibt den Fehler aus, wenn er nicht vorher abgefangen wurde
else:
    print("Das Ergebnis wurde erfolgreich berechnet!")
print("Ende!")
