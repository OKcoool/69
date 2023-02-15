try:
    stream = open('/Dateien/13_1_Produkte.csv', mode='rt', encoding='utf-8')
    ar = stream.readlines()
    dict = {}
    print(ar)
    i = 0
    for j in ar:
        ar[i] = ar[i].replace('\n','')
        ar[i] = ar[i].replace(';',' ')
        ar2 = ar[i].split(' ')
        if ar2[0] in dict:
            dict[ar2[0]] += int(ar2[1])
        else:
            dict[ar2[0]] = int(ar2[1])
        i += 1
    print(dict)
    stream.close()
except Exception as ex:
    print("Datei konnte nicht geöffnet werden", ex)