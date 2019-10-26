def formel (x):
    if 2*x*x+4*x+9 < 50:
        return 2*x*x+4*x+9
    else:
        return 3*x*x+2*x-7

eingabe = eval(input("Bitte eine Zahl eingeben: "))
print(formel(eingabe))
