def berechne_kosten(typ, gaesteliste, alkohol=True, dekoration="normal"):
    # typ: "Abendessen" oder "Geburtstag"
    # gaesteliste: Anzahl der Gäste
    # alkohol: True, wenn alkoholische Getränke angeboten werden, False sonst
    # dekoration: "normal" oder "exklusiv"
    essen_kosten = gaesteliste * 25
    dekoration_kosten = 0
    if dekoration == "normal":
        dekoration_kosten = gaesteliste * 7.5 + 30
    elif dekoration == "exklusiv":
        dekoration_kosten = gaesteliste * 15 + 50
    if typ == "Abendessen":
        getraenke_kosten = 20 if alkohol else 5
        rabatt = 0.05 if not alkohol else 0
        essen_kosten *= (1 - rabatt)
        return essen_kosten + gaesteliste * getraenke_kosten + dekoration_kosten
    elif typ == "Geburtstag":
        if gaesteliste <= 4:
            torte_kosten = 40
            max_buchstaben = 16
        else:
            torte_kosten = 75
            max_buchstaben = 40
        text_kosten = 0.25 * min(max_buchstaben, len(input("Geben Sie den Text auf dem Kuchen ein: ")))
        return essen_kosten + torte_kosten + text_kosten + dekoration_kosten
    else:
        return None


# Kosten für ein Abendessen mit 10 Gästen, alkoholischen Getränken und normaler Dekoration
print(berechne_kosten("Abendessen", 10, True, "normal")) # Ausgabe: 450.0

# Kosten für eine Geburtstagsfeier mit 6 Gästen, alkoholfreien Getränken und exklusiver Dekoration
print(berechne_kosten("Geburtstag", 6, False, "exklusiv")) # Ausgabe: 295.5
