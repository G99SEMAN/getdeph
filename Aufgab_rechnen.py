punkte =0

a = eval(input("Was ist 1+1? :"))
if a == 2:
    punkte +=1
b = eval(input("Was ist 1+2? :"))
if b == 3:
    punkte +=1
c = eval(input("Was ist 1+3? :"))
if c == 4:
    punkte +=1
d = eval(input("Was ist 1+4? :"))
if d == 5:
    punkte +=1
e = eval(input("Was ist 1+5? :"))
if e == 6:
    punkte +=1

if punkte == 5:
    print("Super, alle Aufgaben richtig!")
elif punkte >= 3:
    print("Gute Leistung!")
elif punkte >= 1:
    print("Viele Fehler: weitere Übung erforderlich!")
else:
    print("Dringend Nachhilfe erforderlich!")
