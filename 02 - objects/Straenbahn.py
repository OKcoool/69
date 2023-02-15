class fahrer:
    __name = ""
    __alter = 0

    def get_name(self):
        return self.__name
    def get_alter(self):
        return self.__alter
    def set_alter(self, value):
        self.__alter = value
    def __init__(self, name, alter):
        self.__name = name
        self.__alter = alter
    def __str__(self):
        return f"{self.__name} {self.__alter}"
class strassenbahn:
    __bahnnamen = ""
    __kapazitaet = 0
    __stammlinie = 0
    __fahrer = None

    def get_bahnnamen(self):
        return self.__bahnnamen
    def get_kapazitaet(self):
        return self.__kapazitaet
    def get_stammlinie(self):
        return self.__stammlinie
    def set_stammlinie(self, value):
        self.__stammlinie = value
    def get_fahrer(self):
        return self.__fahrer
    def set_fahrer(self, value):
        self.__fahrer = value

    def __init__(self, name, kapzitaet, stammlinie, fahrer):
        self.__bahnnamen = name
        self.__kapazitaet = kapzitaet
        self.__stammlinie = stammlinie
        self.__fahrer = fahrer

    def __str__(self):
        return self.__bahnnamen + " Kapazität: " + str(self.__kapazitaet) + " Linie: " + str(self.__stammlinie) + " " + str(self.__fahrer)

    def stamm_aendern(self, value):
        self.__stammlinie = value
    def geburtstag(self):
        self.get_fahrer().set_alter(self.get_fahrer().get_alter()+1)
