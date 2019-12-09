class OutOfRangeError(Exception):
    def __init_(self, wert):
        self.Wert = wert


try:
    x = int(input("geben sie eine zahl zwischen 10 und 20 ein:"))
    if x > 20 or x < 10:
        raise OutOfRangeError(x)
    print("Ergebnis:", 4/x)
except OutOfRangeError as fehler:
    print("Die zahl", fehler.Wert, "liegt nicht zwichen 10 und 20")
except ValueError:
    print("Sie müssen eine ganze zahl eingeben!")


print("auf wiedersehen")
print("hello")
