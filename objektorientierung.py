class Auto:
    """
    Erstellt das Objekt Auto für einen Gebrauchtwagenhändler.
    """
    anzahl=0
    def __init__(self, ma, mo, bj, pr):
        """
        Initialisiert ein neues Objekt Auto

        Argumente:
        *Marke (string): Marke des Gebrauchtwagens
        *Modell (string): Modell des Gebrauchtwagens
        *Baujahr (int): Baujahr des Fahrzeugs
        *Preis (int): Angestrebter Verkaufspreis
        """

        self.__Marke = ma
        self.__Modell = mo
        self.__Baujahr = bj
        self.__Preis = pr

        Auto.anzahl +=1

    def getMarke(self):
        """
        Gibt die Marke des Fahrzeugs zurück.
        """
        return self.__Marke
    def getModell(self):
        """
        Gibt das Modell des Fahrzeugs aus
        """
        return self.__Modell

    def getBaujahr(self):
        """
        Gibt das Baujahr des Fahrzeugs aus
        """
        return self.__Baujahr

    def getPreis(self):
        """
        Gibt den Preis des Fahrzeugs aus
        """
        return self.__Preis

    def setPreis(self, preis_neu):
        """
        Ändert den Preis des Fahrzeugs
        """
        if abs(self.__Preis - preis_neu) < self.__Preis *0.05:                  #abs sorgt dafür dass ein - als Vorzeichen keine Auswirkung hat
            self.__Preis = preis_neu
        else:
            print("Die Abweichung zum vorherigen Preis ist sehr groß.")
            bestaetigung = input("Soll %d als neuer Preis festgelegt werden?(ja/nein):"%preis_neu)
            if bestaetigung == "ja":
                self.__Preis = preis_neu

    def __del__(self):
        """
        Löscht das Objekt Auto.
        """
        Auto.anzahl -=1
        print("Auto wurde gelöscht")
        print("Es sind noch %d Autos verfügbar"%Auto.anzahl)

class SUV(Auto):
    """
    Erstellt das Objekt SUV: abgeleitet von der Kasse Auto.
    """
    def __init__(self, ma, mo, bj, pr, allrad):
        """
        Initialisiert ein neues Objekt SUV

        Argumente:
        *Marke (string): Marke des Gebrauchtwagens
        *Modell (string): Modell des Gebrauchtwagens
        *Baujahr (int): Baujahr des Fahrzeugs
        *Preis (int): Angestrebter Verkaufspreis
        *Allradantrieb (bool): Alrad vorhanden?
        """
        Auto.__init__(self, ma, mo, bj, pr)
        self.__Allradantrieb = allrad

    def getAllradamtrieb(self):
        """
        Gibt an, ob ein Allradantrieb vorhanden ist.
        """
        return self.__Allradantrieb




suv1 = SUV("Mercedes Benz", "M63 AMG", 2017, 42000, True)
print(suv1.getAllradantrieb())
print(suv1.getMarke())


# print(Auto.anzahl)
# auto1 = Auto("VW", "Golf", 2011, 5000)
# print(Auto.anzahl, auto1.anzahl)
# auto2 = Auto("Renault", "Clio", 2013, 6000)
# print(Auto.anzahl, auto1.anzahl, auto2.anzahl)
# auto3 = Auto("Posche", "Panamera", 2014, 25000)
# print(Auto.anzahl, auto1.anzahl, auto2.anzahl, auto3.anzahl)

#del auto1      #löscht auch alle anderen Autos
#print(Auto.anzahl, auto2.anzahl, auto3.anzahl)

# wert = eval(input("Geben Sie einen neuen Preis ein: "))
# auto1.setPreis(wert)
#
# print("Neuer Preis:",auto1.getPreis())
