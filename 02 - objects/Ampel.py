class Ampel:
    __zustand = ""

    def get_zustand(self):
        return self.__zustand
    def set_zustand(self, value):
        self.__zustand = value
    def __init__(self, Zustand):
        self.__zustand = Zustand
    def __str__(self):
        return f"Zustand: {self.__zustand}\n{self.getLampen()}"
    def getLampen(self):
        if self.__zustand == "rot":
            return (True, False, False)
        elif self.__zustand == "rotgelb":
            return (True, True, False)
        elif self.__zustand == "gelb":
            return (False, True, False)
        elif self.__zustand == "grün":
            return (False, False, True)
    def schalten(self):
        farben = ["grün","gelb","rot","rotgelb"]
        i=0
        neu=0
        while i<4:
            if farben[i]==self.__zustand:
                neu=i+1
            i+=1
        if neu>3:
            neu=0
        self.__zustand=farben[neu]
        return self.__zustand

class Ampelmanager:
    __ampel0 = None
    __ampel1 = None
    __ampel2 = None
    __ampel3 = None

    def __init__(self):
        self.__ampel0 = Ampel("grün")
        self.__ampel1 = Ampel("rot")
        self.__ampel2 = Ampel("grün")
        self.__ampel3 = Ampel("rot")

    def __str__(self):
        return "Ampel 0:" + self.__ampel0.get_zustand() + "   Ampel 1:" + self.__ampel1.get_zustand() + "   Ampel 2:" + self.__ampel2.get_zustand() + "   Ampel 3:" + self.__ampel3.get_zustand()
    def schalten(self):
        self.__ampel0.schalten()
        self.__ampel1.schalten()
        self.__ampel2.schalten()
        self.__ampel3.schalten()