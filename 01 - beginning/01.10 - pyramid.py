count = int(input("Blöcke: "))
i = 1
height = 0
while ((count - i) >= 0):
    height = height + 1
    count = count - i
    i = i + 1
print("Height: ", height)
