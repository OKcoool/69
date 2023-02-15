from Vorsatz import Vorsatz, Verwaltung

vorsatz1 = Vorsatz("Sparen", 100, 30) # Case Sensitive bei Abfrage
vorsatz2 = Vorsatz("kein Alkohol", 0, 60) #Eigentlich trinke ich sowieso kein Alkohol
vorsatz3 = Vorsatz("Fitness", 0, 40)
meineliste = Verwaltung()
meineliste.add_vorsatz(vorsatz1)
meineliste.add_vorsatz(vorsatz2)
meineliste.add_vorsatz(vorsatz3)
#Umsetzung
meineliste.vorsatzumgesetzt("Sparen", 5)
meineliste.vorsatzumgesetzt("Fitness", 15)
meineliste.vorsatzumgesetzt("Fitness", 5)
meineliste.vorsatzumgesetzt("kein Alkohol", 30)
meineliste.vorsatzumgesetzt("Sparen", 5)
#Ausgabe
print("Gesamtkosten:")
print(meineliste.gesamtkosten())
print("Gesamterreichungsgrad:")
print(meineliste.gesamterreichungsgrad())
print("Alle Vorsätze:")
print(meineliste)