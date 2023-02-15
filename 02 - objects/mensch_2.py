class haustier:
    __art = 0
    __farbe = ""
    __futter = ""

    def get_art(self):
        return self.__art
    def get_farbe(self):
        return self.__farbe
    def get_futter(self):
        return self.__futter
    def set_futter(self, value):
        self.__futter = value
    def __init__(self, art, farbe, futter):
        self.__art = art
        self.__farbe = farbe
        self.__futter = futter
    def __str__(self):
        return f"{self.__art}/{self.__farbe}/{self.__futter}\n"
class mensch:
    __alter = 0
    __vorname = ""
    __nachname = ""
    __famileinstand = ""
    __haustier = None

    def get_alter(self):
        return self.__alter
    def get_vorname(self):
        return self.__vorname
    def get_nachname(self):
        return self.__nachname
    def set_nachname(self, value):
        self.__nachname = value
    def get_familienstand(self):
        return self.__famileinstand
    def get_haustier(self):
        return self.__haustier
    def set_haustier(self, value):
        self.__haustier = value
    def __init__(self, nachname, vorname, alter, fammilenstand, haustier):
        self.__nachname = nachname
        self.__vorname = vorname
        self.__alter = alter
        self.__famileinstand = fammilenstand
        self.__haustier = haustier
    def __str__(self):
        return self.__nachname + " " + str(self.__haustier)
    def geburtstag(self):
        self.__alter += 1
    def heiraten(self, Nachname):
        if self.__famileinstand == "verheiratet":
            print("Diese Person ist schon verheiratet")
            return False
        if self.__famileinstand == "ledig":
            self.__nachname = Nachname
            self.__famileinstand = "verheiratet"
            return True