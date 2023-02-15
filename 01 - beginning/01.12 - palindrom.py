word = input("eingabe: ")
word = word.upper()
word = word.replace(" ", "")
if str(word) == str(word)[::-1]:
    print(word, "ist ein Palindrom")
else:
    print(word, "ist kein Palindrom")
