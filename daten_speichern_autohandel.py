class Auto:
    """
    Erstellt das Objekt Auto für einen Gebrauchtwagenhändler.
    """
    def __init__(self, ma, mo, bj, pr):
        """
        Initialisiert ein neues Objekt Auto

        Argumente:
        * Marke (string): Marke des Gebrauchtwagen
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
         gibt die Marke des Autos zurück
         """
         return self.__Marke

    def getModell(self):
        """
        gibt das Modell des Autos zurück
        """
        return self.__Modell

    def getBaujahr(self):
        """
        gibt das Baujahr des Autos zurück
        """
        return self.__Baujahr

    def getPreis(self):
        """
        gibt den Preis des Autos zurück
        """
        return self.__Preis

    def setPreis(self, preis_neu):
        """
        ändert den Preis des Autos
        """
        if abs(self.__Preis - preis_neu) < self.__Preis * 0,05:
            self.__Preis = preis_neu
        else:
            print("Die Abweichung zum vorherigen Preis ist sehr groß.")
            bestaetigung = input("Soll %d als neuer Preis festgelegt werden= (y/n)", %preis_neu)
            if bestaetigung == "y":
                self.__Preis = preis_neu
