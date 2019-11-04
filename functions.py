def formel (x):
    if 2*x*x+4*x+9 < 50:
        return 2*x*x+4*x+9
    else:
        return 3*x*x+2*x-7


def zweierschritte(z1, z2):
    if z1 < z2:
        for i in range(z1, z2+1, 2):
            print(i)
    else:
        for i in range(z1, z2-1, -2):
            print(i)

def registrarion(username, password):       #Kapitel 9
    userlist = [("kevin", "lol"), ("ramona", "mallorca"), ("name", "passwort")]
    for zugang in userlist:
        if username == zugang[0] and password == zugang[1]:
            print("Eingeloggt!!")
            return True

    print("Nutzername oder Passwort falsch!")
    return False


def nameage(name, age):
    print("hello", name, "you are", age, "years old!")


import random

def wuerfeln():
    return random.randint(1, 6)

import time

def datum():
    return time.strftime("%d.%m.%Y")
def zeit():
    return time.strftime("%H:%M:%S")
