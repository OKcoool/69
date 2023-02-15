height = float(input("Bitte Größe eingeben (m): "))
weigth = float(input("Bitte Gewicht eingeben (kg): "))

bmi = weigth / (height * height)

if bmi < 18.5:
    print("untergewicht")
elif bmi < 24.9:
    print("normalgewicht")
elif bmi < 29.9:
    print("übergewicht")
elif bmi < 34.9:
    print("adipositas grad 1")
else:
    print("adipositas grad 2")
