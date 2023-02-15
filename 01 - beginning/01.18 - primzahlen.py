def is_prime(i):
    isPrime = True
    for x in range(2, int(i / 2 + 1)):

        if i / x == int(i / x):
            isPrime = False
    if i == 1:
        isPrime = False
    return isPrime


zahl = int(input("E:"))

if is_prime(zahl) is True:
    print("Ist eine Primzahl")
else:
    print("Ist keine Primzahl")
