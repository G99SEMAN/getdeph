class Flat:
    """
    Generate an object Flat
    """

    anzahl = 0
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

        Flat.anzahl += 1

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


wohnung1 = Flat("NiehlerHafen", "Am Niehler Hafen 3", 3, 90)
wohnung2 = Flat("Bechen", "Heiderjansfelderstr. 35", 4, 120)
wohnung3 = Flat("Köln", "Freiligrathstr. 12", 2, 400)
wohnungen = [wohnung1, wohnung2, wohnung3]

#print(type(Flat.anzahl))
for i in range(Flat.anzahl):
    print("Wohnung", i+1, ":", wohnungen[i].getName(),",", wohnungen[i].getStrasse(), ", Betten:", wohnungen[i].getBetten(), ", Preis pro Übernachtung:", wohnungen[i].getPreis())


#print(wohnung1.getPreis())
