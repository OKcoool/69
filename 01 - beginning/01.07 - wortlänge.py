print("Welches Wort ist länger?")
word = input("Bitte geben sie das erste Wort ein: ")
word1 = input("Bitte geben sie das zweite Wort ein: ")

w = len(word)
w1 = len(word1)

if w > w1:
    print("Das erste Wort ist länger")
elif w < w1:
    print("Das zweite Wort ist länger")
else:
    print("Die Wörter sind gleichlang.")
