class Auto:
    """
    Erstellt das Objekt Auto für einen Gebrauchtwagenhändler.
    """
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
        if abs(self.__Preis - preis_neu) < self.__Preis *0.05:
            self.__Preis = preis_neu
        else:
            print("Die Abweichung zum vorherigen Preis ist sehr groß.")
            bestaetigung = input("Soll %d als neuer Preis festgelegt werden?(ja/nein):"%preis_neu)
            if bestaetigung == "ja":
                self.__Preis = preis_neu



auto1 = Auto("VW", "Golf", 2011, 5000)
auto2 = Auto("Renault", "Clio", 2013, 6000)
auto3 = Auto("Posche", "Panamera", 2014, 25000)

wert = eval(input("Geben Sie einen neuen Preis ein: "))
auto1.setPreis(wert)

print("Neuer Preis:",auto1.getPreis())
