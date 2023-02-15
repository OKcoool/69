# Marco Schmidt FIS11 01.02.2023
class Datum:
    __tag = 0
    __monat = 0

    def __init__(self, tag, monat):
        self.__tag = tag
        self.__monat = monat

    def __str__(self):
        return "{:02d}.{:02d}".format(self.__tag, self.__monat)


class Lebensmittel:
    __bezeichung = ""
    __mhd = 0
    __einkaufspreis = 0.0
    __lagerplatz = 0

    def __init__(self, bezeichnung, mhd, einkaufspreis):
        self.__bezeichnung = bezeichnung
        self.__mhd = mhd
        self.__einkaufspreis = einkaufspreis
        self.__lagerplatz = 0

    def haltbar(self, heute):
        vergleich = (self.__mhd.monat - heute.monat) + 30 * (self.__mhd.tag - heute.tag)
        return vergleich >= 0

    def __str__(self):
        return "{} ({}) - Lagerplatz {}".format(self.__bezeichnung, str(self.__mhd), self.__lagerplatz)

    def get_bezeichnung(self):
        return self.__bezeichnung

    def get_mhd(self):
        return self.__mhd

    def get_einkaufspreis(self):
        return self.__einkaufspreis

    def set_lagerplatz(self, lagerplatz):
        self.__lagerplatz = lagerplatz


class Lager:
    __Lager = []
    __lagerplatz = 0

    def __init__(self):
        self.__lager = []
        self.__lagerplatz = 0

    def add(self, lebensmittel):
        self.__lager.append(lebensmittel)
        self.__lagerplatz += 1
        lebensmittel.set_lagerplatz(self.__lagerplatz)

    def pick(self, bezeichnung):
        artikel = [x for x in self.__lager if x.get_bezeichnung() == bezeichnung]
        artikel.sort(key=lambda x: x.get_mhd().tag + 30 * x.get_mhd().monat)
        return artikel[0]

    def bereinigung(self):
        heute = Datum(1, 2)
        abschreibung = 0
        lager = [x for x in self.__lager if x.haltbar(heute)]
        abschreibung = len(self.__lager) - len(lager)
        self.__lager = lager
        return abschreibung

    def lagerausgabe(self):
        for artikel in self.__lager:
            print(artikel)


# Main
lager = Lager()

artikel1 = Lebensmittel("Milch", Datum(28, 1), 1.0)
artikel2 = Lebensmittel("Milch", Datum(5, 2), 0.5)
artikel3 = Lebensmittel("Ei", Datum(6, 2), 0.1)
artikel4 = Lebensmittel("Joghurt", Datum(27, 6), 1.99)
artikel5 = Lebensmittel("Kaese", Datum(13, 3), 0.8)
artikel6 = Lebensmittel("Wurst", Datum(12, 1), 1.99)

lager.pick("Joghurt")
lager.pick("Wurst")

lager.bereinigung()

lager.lagerausgabe()
