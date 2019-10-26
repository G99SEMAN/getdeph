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
