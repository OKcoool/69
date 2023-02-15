def checkpwd(pw):
    i = 0
    num = len(pw)

    if num >= 8: #längenprüfung
        i += 1
    if pw.isalnum() is False: #sonderzeichenprüfung
        i += 1
    if pw.isalpha() is False: #nummernprüfung
        i += 1

    return


pw = input("Passwort?: ")
check = False

if checkpwd(pw) is True:
    print("Passwort gespeichert!")
else:
    print("Passwort zu schwach!")