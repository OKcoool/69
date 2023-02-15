pin = [1, 1, 1, 1]
check = True

for x in pin:
    inp = int(input("Bitte geben Sie Ihren PIN ein: "))
    if x != inp:
        check = False

if check is True:
    print("Hello User")
else:
    print("Schmutz bleibt draußen!")
