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

        self.Marke = ma
        self.Modell = mo
        self.Baujahr = bj
        self.Preis = pr
        
