import math

numb = int(input("Wurzel von Zahl: "))

if numb % 2 == 0:
    print(math.sqrt(numb))
else:
    print(math.sqrt(numb) + 1)
