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


userlist1 = {"username": "name1", "password": "password1"}
userlist2 = {"username": "name2", "password": "password2"}
userlist3 = {"username": "name3", "password": "password3"}
userlist4 = {"username": "name4", "password": "password4"}
userlist5 = {"username": "name5", "password": "password5"}


def pwcheck(user, pw):
    if user == userlist1["username"] and pw == userlist1["password"]:
        print("Eingeloggt!!")
    else:
        print('Benutzername oder Passwort falsch!')
