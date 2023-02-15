from mensch_2 import mensch, haustier

def ausgabe(obj):
    print(obj.get_vorname(), end=" ")
    print(obj.get_nachname(), end=" ")
    print(obj.get_alter(), "Jahre", end=" ")
    print(obj.get_familienstand(), end=" ")
    print(obj.get_haustier())

ich = mensch("Kistner","Paul",18,"ledig",haustier("Katze","Schwarz-braun","Käse"))
ratti = haustier("Olaf","Grau","Müll")
ichFranz = mensch("Franz","Schmitt",20,"ledig",ratti)

# Ausgabe
print(ich)
print(ichFranz)
ich.get_haustier().set_futter("Maus")
print(ich)
#print(ich.get_haustier().get_art())
#print(ich.get_haustier().get_futter())
#print(ich.get_haustier().get_farbe())
