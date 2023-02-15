storage = {
    "Bourbon": 0,
    "Schokolade": 5,
    "Erdbeeren": 3,
    "Hopfenblütentee": 1,
    "Lasagne": 0,
    "Himbeeren": 4,
    "Eis": 7,
    "Litschi": 0
}

for key in storage.keys():
    print(key, "->", storage[key])
    if storage[key] == 0:
        bst = int(input("Ist leer, bitte nachbestellen: "))
        storage[key] = bst
