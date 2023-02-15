try:
    stream = open("/FPA/vokabel.txt", mode='rt', encoding='utf-8')
    ary = stream.readlines()
    stream.close()
except:
    print("Error Opening")

dictionary = {}
wrong = 0
good = 0

for i in ary:
    ary2 = i.strip('\n').split(';')
    dictionary[ary2[0]] = ary2[1]
    

for ger, eng in dictionary.items():
    guess = input("Übersetze das auf Englisch " + ger + "?\n")
    if guess == eng:
        good = good + 1
    else:
        wrong = + 1


prt = float(good)/(good + wrong) * 100

if prt < 50:
    print(prt, "Schlecht.")
elif prt < 86:
    print(prt, "ok.")
else:
    print(prt, "super")
