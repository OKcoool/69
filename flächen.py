import math


class Figur:
    def __init__(self, kanten):
        self.kanten = kanten
        self.umfang = 0
        self.flaecheninhalt = 0

    def berechneUmfang(self):
        pass

    def berechneFlaecheninhalt(self):
        pass


class Kreis(Figur):
    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius

    def berechneUmfang(self):
        self.umfang = 2 * math.pi * self.radius
        return self.umfang

    def berechneFlaecheninhalt(self):
        self.flaecheninhalt = math.pi * (self.radius ** 2)
        return self.flaecheninhalt


class Rechteck(Figur):
    def __init__(self, laenge, breite):
        super().__init__(4)
        self.laenge = laenge
        self.breite = breite

    def berechneUmfang(self):
        self.umfang = 2 * (self.laenge + self.breite)
        return self.umfang

    def berechneFlaecheninhalt(self):
        self.flaecheninhalt = self.laenge * self.breite
        return self.flaecheninhalt


class Dreieck(Figur):
    def __init__(self, a, b, c, hoehe):
        super().__init__(3)
        self.a = a
        self.b = b
        self.c = c
        self.hoehe = hoehe

    def berechneUmfang(self):
        self.umfang = self.a + self.b + self.c
        return self.umfang

    def berechneFlaecheninhalt(self):
        self.flaecheninhalt = 0.5 * self.hoehe * self.b
        return self.flaecheninhalt


kreis1 = Kreis(1)
rechteck1 = Rechteck(2, 2)
dreieck1 = Dreieck(2, 2, 2, 2)

print(kreis1.berechneUmfang(),
      kreis1.berechneFlaecheninhalt(),
      rechteck1.berechneUmfang(),
      rechteck1.berechneFlaecheninhalt(),
      dreieck1.berechneUmfang(),
      dreieck1.berechneFlaecheninhalt())
