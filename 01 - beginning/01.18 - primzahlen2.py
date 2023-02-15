def is_prime(i):
    prym = True
    for x in range(2, int(i / 2 + 1)):

        if i / x == int(i / x):
            prym = False

    if i == 1:
        prym = False
    return prym


for a in range(1, 1000):
    if is_prime(a) is True:
        print(a)
