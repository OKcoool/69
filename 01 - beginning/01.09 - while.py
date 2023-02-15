fak = int(input("Bitte geben Sie die Zahl ein: "))
num = 1
pri = fak

while fak > 1:
    num *= fak
    fak -= 1

print(str(pri) + '! =', num)
