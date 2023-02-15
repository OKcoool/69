class Zug:
    __startort = ""
    __fahrzeit = 0  # in minuten
    __preis = 0.0  # in euro
    __verspaetung = 0  # in minuten

    def getStartort(self):
        return self.__startort

    def setStartort(self, startort):
        self.__startort = startort

    def getFahrzeit(self):
        return self.__fahrzeit

    def getPreis(self):
        return self.__preis

    def getVerspaetung(self):
        return self.__verspaetung

    def __init__(self, startort, preis, fahrzeit):
        self.__startort = startort
        self.__preis = preis
        self.__fahrzeit = fahrzeit

    def ankunft(self, gesamtfahrzeit):
        self.__verspaetung = gesamtfahrzeit - self.__fahrzeit

    def entschaedigung(self):
        if self.__verspaetung > 29:
            return self.__preis * 0.1
        if self.__verspaetung > 59:
            return self.__preis * 0.3
        return 0

    def __str__(self):
        ausgabe = "Der Zug aus " + self.getStartort() + " ist eingetroffen. "

        if self.__verspaetung > 0:
            verspH = round(self.__verspaetung / 60, None)
            verspM = self.__verspaetung % 60
            ausgabe += "er hatte " + str(verspH) + " Stunde(n) und " + str(verspM) + " Minute(n) verspätung. "
        else:
            ausgabe += "er war pünktlich. "
        return ausgabe


class Bahnhof:
    __zugliste = None

    def __init__(self):
        self.__zugliste = list()

    def addZug(self, zug):
        self.__zugliste.append(zug)

    def removeZug(self, start):
        for k in self.__zugliste:
            if k.getStartort() == start:
                self.__zugliste.remove(k)

    def gesamtentschaedigung(self):
        ges = 0
        for k in self.__zugliste:
            ges += k.entschaedigung()
        print("Der Betrag des gesamten zu erstattenden Betrags beträgt: ", ges)

    def prozentualeVerspaetung(self):
        sum = 0
        late = 0
        for k in self.__zugliste:
            sum += k.getFahrzeit()
            if k.getVerspaetung() > 0:
                late += k.getFahrzeit() + k.getVerspaetung()
        return late / sum * 100 - 100

    def __str__(self):
        ausgabe = ""

        for k in self.__zugliste:
            ausgabe += str(k)
        return ausgabe


bhof = Bahnhof()

zug1 = Zug("Bamberg", 15.00, 60)
zug2 = Zug("München", 30.00, 120)
zug3 = Zug("Hamburg", 50.00, 500)
zug4 = Zug("Kitzingen", 12.50, 15)

bhof.addZug(zug1)
bhof.addZug(zug2)
bhof.addZug(zug3)
bhof.addZug(zug4)

zug1.ankunft(65)
zug2.ankunft(120)
zug3.ankunft(580)
zug4.ankunft(45)

bhof.removeZug("München")

bhof.gesamtentschaedigung()

print("Die Prozentuale Verspätung aller Züge beträgt: ", bhof.prozentualeVerspaetung())

print(bhof)