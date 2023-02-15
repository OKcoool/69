class PKW:
    __aktuelleFuellung = 0
    __baujahr = 0
    ___farbe = ""
    __kmstand = 0
    __marke = ""
    __maxfuellstand = 0
    __sitze = 0
    __verbrauch = ""

    def get_AktuelleFuellung(self):
        return self.__aktuelleFuellung

    def get_Baujahr(self):
        return self.__baujahr

    def get_Farbe(self):
        return self.___farbe

    def get_Kmstand(self):
        return self.__kmstand

    def get_Marke(self):
        return self.__marke

    def get_MaxFuellstand(self):
        return self.__maxfuellstand

    def get_Sitze(self):
        return self.__sitze

    def get_Verbrauch(self):
        return self.__verbrauch

    def Fahren(self, value):
        if ((value / 100) * self.__verbrauch) <= self.__aktuelleFuellung:
            self.__aktuelleFuellung = self.__aktuelleFuellung - ((value / 100) * self.__verbrauch)
            self.__kmstand = self.__kmstand + value
            print("Gefahren")
        else:
            print("Nicht genug Sprit!")

    def Tanken(self, value):
        if (self.__aktuelleFuellung + value) <= self.__maxfuellstand:
            self.__aktuelleFuellung = self.__aktuelleFuellung + value
            print("Getankt!")
        else:
            print("Wert übersteigt den maximalen Füllstand!")

    def __init__(self, verbrauch, farbe, sitze, marke, maxfüllstand, baujahr, kmstand):
        self.__verbrauch = verbrauch
        self.___farbe = farbe
        self.__sitze = sitze
        self.__marke = marke
        self.__maxfuellstand = maxfüllstand
        self.__baujahr = baujahr
        self.__kmstand = kmstand

    def __str__(self):
        return "Km-Stand: " + str(self.__kmstand) + "\nAktuelle Tankfüllung: " + str(self.__aktuelleFuellung)
