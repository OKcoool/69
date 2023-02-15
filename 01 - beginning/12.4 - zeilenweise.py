try:
    stream = open('/Dateien/Namen.txt', mode="rt", encoding="utf-8")
    line = stream.readline()
    i = 0
    array = [str("") for x in range(12)]
    index = 0

    while line != '':
        line = line.replace("\n", "")
        array[i] = str(line)
        line = stream.readline()
        i += 1
    array.sort()
    print(array)

    for i in range(26):
        var = 0
        index = 0
        for j in range(12):
            var = var + int(array[index].count(chr(65 + i)))
            index = index + 1
        print(var, "x ", chr(65 + i))

except Exception as ex:
    print("Cannot open file: ", ex)
