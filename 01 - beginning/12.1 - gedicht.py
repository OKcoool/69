try:
    i = 0
    cho = input("Welches Gedicht wollen sie haben: ")
    cho += '.txt'
    stream = open('../Dateien/' + cho, mode="rt", encoding="utf-8")
    print(stream.read())

    text = open("../Dateien/" + cho).read()
    result = len(text.strip().split())
    print("\nEs sind ", result, " Woerter im Gedicht")

    for j in text:
        if j.isalnum() is True:
            i += 1

    schnitt = int(i) / int(result)
    print("\nDie Durschnittslaenge ist", schnitt)
    stream.close()

except Exception as ex:
    print("Cannot open file: ", ex)
