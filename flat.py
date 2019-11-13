class Flat:
    """
    Generate an object Flat
    """

    def __init__(self, na, st, be, pr):
        """
        initialize a new object Flat

        Argumente:
        *Name (string):     Name der Wohnung
        *Strasse (string):  Name der Strasse
        *Betten (int):      Anzahl der Betten
        *Preis (int):       Preis pro Übernachtung
        """

        self.__Name = na
        self.__Strasse = st
        self.__Betten = be
        self.__Preis = pr

    def getName(self):
        """
        Gibt den Name der Wohnung aus
        """
        return self.__Name

    def getStrasse(self):
        """
        Gibt den Namen der Strasse aus
        """
        return self.__Strasse

    def getBetten(self):
        """
        Gibt die Anzahl der Betten aus
        """
        return self.__Betten

    def getPreis(self):
        """
        Gibt den Preis der Wohnung pro Übernachtung aus
        """
        return self.__Preis

    def setPreis(self, preis_neu):
        """
        Ändert den Preis der Wohnung
        """
        if abs(self.__Preis - preis_neu) < self.__Preis *0.05:                  #abs sorgt dafür dass ein - als Vorzeichen keine Auswirkung hat
            self.__Preis = preis_neu
        else:
            print("Die Abweichung zum vorherigen Preis ist sehr groß.")
            bestaetigung = input("Soll %d als neuer Preis festgelegt werden?(ja/nein):"%preis_neu)
            if bestaetigung == "ja":
                self.__Preis = preis_neu
    
