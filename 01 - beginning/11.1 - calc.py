def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def mal(x, y):
    return x * y


def geteilt(x, y):
    return x / y


try:
    cho = int(input("Was möchten sie rechnen?\n"
                    "1. Plus\n"
                    "2. Minus\n"
                    "3. Mal\n"
                    "4. Geteilt\n"
                    "E: "))

    z1 = float(input("Zahl 1: "))
    z2 = float(input("Zahl 2: "))

    if cho == 1:
        erg = plus(z1, z2)
    elif cho == 2:
        erg = minus(z1, z2)
    elif cho == 3:
        erg = mal(z1, z2)
    elif cho == 4:
        erg = geteilt(z1, z2)
    else:
        erg = 0
        print("Falsche Auswahl")
    print("Das Ergebnis lautet:", erg)

except ValueError:
    print("Bitte gueltige Zahl eingeben")
except ZeroDivisionError:
    print("Teilung durch 0 nicht moeglich")
except:
    print("ERROR!")
