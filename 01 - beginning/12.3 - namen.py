try:
    stream = open("../Dateien/Namen.txt", mode="rt", encoding="utf-8")
    line = stream.readline()
    i = 0
    array = [[str("") for x in range(4)] for y in range(3)]
    index = 0
    while line != '':
        line = line.replace("\n", "")
        array[index][i] = str(line)
        line = stream.readline()
        i += 1
        if i == 4:
            index = index + 1
            i = 0
    print(array)

except Exception as ex:
    print("Cannot open file: ", ex)
