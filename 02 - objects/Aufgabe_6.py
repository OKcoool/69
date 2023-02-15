try:
    stream = open("../Dateien/vokabel.txt", mode="rt", encoding="utf-8")
    stream2 = open("../Dateien/vokabel2.xml", mode="wt", encoding="utf-8")
    stream2.write('<?xml version="1.0" encoding="UTF-8"?>\n'+'<Vokabelliste>\n')
    ar = stream.readlines()
    i = 0
    for j in ar:
        ar[i] = ar[i].replace('\n', '')
        ar[i] = ar[i].replace(';', ' ')
        ar2 = ar[i].split(' ')
        stream2.write('\t<Vokabel>\n')
        stream2.write('\t\t<deutsch>'+ar2[0]+'</deutsch>\n')
        stream2.write('\t\t<english>'+ar2[1]+'</english>\n')
        stream2.write('\t</Vokabel>\n')
        i += 1
    stream2.write('</Vokabelliste>\n')
    stream.close()
    stream2.close()
except Exception as ex:
    print("Datei konnte nicht geöffnet werden", ex)
