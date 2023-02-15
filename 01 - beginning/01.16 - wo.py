inp = int(input("number: "))
num = []
i = 0
for x in range(0, 100, 1):
    num.append(x)
    i += 1
i = 0
while inp != num[i]:
    i += 1
print(num[i])
