def check(yearcheck):
    if yearcheck % 4 == 0 and yearcheck % 100 != 0 or yearcheck % 400 == 0:
        return True


for year in range(1900, 2200):
    if check(year) is True:
        print(year, end=" ")
