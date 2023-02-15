import random

a = random.randrange(1, 100, 1)
flag = False
i = 0
while flag is not True and i < 9:
   b = int(input("Zahl eingeben: "))
   if a > b:
       print("Zahl ist größer")
   elif a < b:
       print("Zahl ist kleiner")
   else:
       print("RICHTIG KEULE!")
       flag = True

if flag is False:
    print("zu viele versuche", "Die zahl war", a)
