a = int(input("a:"))
b = int(input("b:"))
x1 = int(input("Anfang:"))
x2 = int(input("Ende:"))
x2 += 1
print("x->y")
for x in range(x1, x2):
    print(x, "->", a * x + b)
