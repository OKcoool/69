class Weinachtsgeschenk:
    __name = ""
    __preis = 0
    __verkaufsladen = ""

    def __init__(self, Name, Preis, Verkaufsladen):
        self.__name = Name
        self.__preis = Preis
        self.__verkaufsladen = Verkaufsladen
    def get_name(self):
        return self.__name
    def get_preis(self):
        return self.__preis
class Wunschzettel:
    __Wunschzettel = []

    def __init__(self):
        self.__Wunschzettel = list()

    def add_geschenk(self):
        self.__Wunschzettel.append(Weinachtsgeschenk(input("Name:"), input("Preis:"), input("Verkaufsladen:")))

    def delete_geschenk(self):
        eingabe = input("Name:")
        self.__Wunschzettel.remove(next(w for w in self.__Wunschzettel if w.get_name() == eingabe))
        print("Geschek", eingabe, "wurde gelöscht")
    def gesamtkosten(self):
        gesamt = 0
        for x in self.__Wunschzettel:
            gesamt += float(x.get_preis())
        return gesamt
    def menge_Geschenke(self):
        return len(self.__Wunschzettel)