import random
import operator

try:
    try:
        stream = open('../Dateien/Highscore.csv', mode='rt', encoding='utf-8')
        ar = stream.readlines()
        stream.close()
    except:
        stream = open('../Dateien/Highscore.csv', mode='wt', encoding='utf-8')
        stream.close()
        ar = []
    dict = {}
    i = 0
    for j in ar:
        ar[i] = ar[i].replace('\n', '')
        ar[i] = ar[i].replace(';', ' ')
        ar2 = ar[i].split(' ')
        dict[ar2[0]] = int(ar2[1])
        i += 1
    i = 0
    Spielername = input("Bitte geben Sie Ihren Spielernamen ein: ")
    zahl = random.randrange(1, 100 + 1, 1)
    counter = 0
    win = False
    while 1 != 2 and win != True:
        eingabe = int(input("Bitte geben Sie eine Zahl ein: "))
        if eingabe == zahl:
            print("Sie haben die Zahl erraten")
            win = True
            dict[Spielername] = counter
            break
        elif eingabe > zahl:
            print("Die Zahl ist kleiner als die Eingabe!")
        elif eingabe < zahl:
            print("Die Zahl ist größer als die Eingabe!")
        counter += 1
    sorted = sorted(dict.items(), key=operator.itemgetter(1))
    stream = open('../Dateien/Highscore.csv', mode='wt', encoding='utf-8')
    for i in range(len(sorted)):
        stream.write(str(sorted[i][0]) + ';' + str(sorted[i][1]) + '\n')
    stream.close()
except Exception as ex:
    print("Datei konnte nicht geöffnet werden", ex)
