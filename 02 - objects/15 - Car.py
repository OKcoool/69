from classCar import PKW

Auto = PKW(8.5, "Blau", 5, "Lamorghini", 80, 2019, 156345)
Auto.Tanken(50)
print("Stand vor Fahrt\n")
print(Auto)
Auto.Fahren(300)
print("Stand dannach\n")
print(Auto)
