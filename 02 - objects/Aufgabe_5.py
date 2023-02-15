try:
    Vorname = input("Vorname: ")
    Nachname = input("Nachname: ")
    Straße = input("Straße: ")
    Hausnummer = input("Hausnummer: ")
    PLZ = input("PLZ: ")
    Ort = input("Ort: ")
    stream = open(Vorname + Nachname +".txt", mode="wt", encoding="utf-8")
    stream.write(Vorname + ' ' + Nachname + '\n' + Straße + ' ' + Hausnummer + '\n' + PLZ + ' ' + Ort)
    stream.close()
except:
    print("Datei konnte nicht geöffnet werden")
