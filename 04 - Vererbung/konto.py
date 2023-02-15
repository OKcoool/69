class Konto:
    def __init__(self, kontonummer, kontostand=0, minimum=-1000):
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self.minimum = minimum

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def auszahlen(self, betrag):
        if self.kontostand - betrag >= self.minimum:
            self.kontostand -= betrag
            return True
        else:
            return False


class Sparkonto(Konto):
    def __init__(self, kontonummer, zinssatz, maxauszahlung, kontostand=0, minimum=-1000):
        Konto.__init__(self, kontonummer, kontostand, minimum)
        self.zinssatz = zinssatz
        self.maxAuszahlung = maxauszahlung

    def auszahlen(self, betrag):
        if betrag <= self.maxAuszahlung and self.kontostand - betrag >= self.minimum:
            self.kontostand -= betrag
            return True
        else:
            return False

    def zinsengutschreiben(self):
        zinsbetrag = self.kontostand * self.zinssatz / 100
        self.kontostand += zinsbetrag

