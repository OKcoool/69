from Wunschzettel import Wunschzettel

Wunschzettel = Wunschzettel()
for i in range(5):
    Wunschzettel.add_geschenk()

print(Wunschzettel.menge_Geschenke())
print(Wunschzettel.gesamtkosten())
Wunschzettel.delete_geschenk()