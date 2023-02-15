class Vorsatz:
    __beschreibung = ""
    __kosten = 0
    __durchaltedauer = 0
    __erreichungsgrad = 0

    def __init__(self, beschreibung, kosten, durchhaltedauer):
        self.__beschreibung = beschreibung
        self.__kosten = kosten
        self.__durchaltedauer = durchhaltedauer #Tage
        #Erreichungsgrad standard 0 nicht nötig noch mal zu setzen

    def __str__(self):
        return self.__beschreibung + " wurde zu " + str(self.__erreichungsgrad) + " Prozent erreicht "

    def get_beschreibung(self):
        return self.__beschreibung

    def set_beschreibung(self, beschreibung):
        self.__beschreibung = beschreibung

    def get_kosten(self):
        return self.__kosten

    def get_durchhaltedauer(self):
        return self.__durchaltedauer

    def get_erreichungsgrad(self):
        return self.__erreichungsgrad

    def erreicht(self, tage):
        prozent = tage * 100 / self.__durchaltedauer
        if self.__erreichungsgrad + prozent <= 100:
            self.__erreichungsgrad = self.__erreichungsgrad + prozent
        else:
            print("Erreichtgrad geht über 100%") # ich weiß print ist nicht optimal aber ich habs halt so

class Verwaltung:
    __vorsatliste = None

    def __init__(self):
        self.__vorsatliste = list()

    def __str__(self):
        string = ""
        for objekt in self.__vorsatliste:
            string = string + str(objekt) + "/ " # / ist die Trennung zwischen den einzelnen Vorsätzen würde auch mit \n gehen
        return string
    
    def add_vorsatz(self, vorsatz: Vorsatz):
        self.__vorsatliste.append(vorsatz)

    def vorsatzumgesetzt(self, beschreibung, tage): 
        for objekt in self.__vorsatliste:
            if objekt.get_beschreibung() == beschreibung:
                objekt.erreicht(tage)
    
    def gesamtkosten(self):
        geskosten = 0
        for objekt in self.__vorsatliste:
            geskosten = geskosten + objekt.get_kosten()
        return geskosten
    
    def gesamterreichungsgrad(self):
        geserreich = 0
        zaehler = 0
        for objekt in self.__vorsatliste:
            zaehler = zaehler + 1
            geserreich = geserreich + objekt.get_erreichungsgrad()
        geserreich = geserreich / zaehler
        return geserreich