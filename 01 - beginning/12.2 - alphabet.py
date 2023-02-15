try:
    stream = open("../Dateien/alphabet.txt", encoding="utf-8")
    letter = stream.read(1)
    i = 1
    while letter != '':
        z2 = letter.upper()
        print(z2, "->", ord(z2), end="\t")
        print(letter, "->", ord(letter))
        i += 1
        letter = stream.read(1)
    print("\nCunter: " + str(i))
    stream.close()

except Exception as ex:
    print("Cannot open file: ", ex)
