"""
Übungsaufgabe 1
"""

# try:
#     z1 = int(input("Bitte geben sie die erste zahl ein:"))
#     z2 = int(input("Bitte geben sie die zweite zahl ein:"))
#
#     print(z1/z2)
#
# except ZeroDivisionError:
#     print("Sie können nicht durch 0 teilen!")
# except ValueError:
#     print("Sie müssen eine Zahl eingeben")
# except:
#     print("Folgender Fehler ist aufgetreten:", sys.exc_info()[0])               #gibt den Fehler aus, wenn er nicht vorher abgefangen wurde
#
# print("Ende!")



"""
Übungsaufgabe 2
"""

class OddError(Exception):
    def __init__(self, wert):
        self.Wert = wert

try:
    wort = input("geben sie ein wort mit einer geraden anzahl an buchstaben ein: ")
    if len(wort) %2 == 1:
        raise OddError(wort)
    mitte = int(len(wort)/2)
    teil1 = wort[:mitte]
    teil2 = wort[mitte:]
    print("Erste Hälfte:", teil1)
    print("Zweite Hälfte:", teil2)

except OddError as fehler:
    print('Das Wort "'+wort+'" hat eine ungerade Anzahl an buchstaben.')

print("Auf wiedersehen!")
print("hello world")