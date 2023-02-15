eing=int(input('Eingabe:'))
t=0
i=1

while i<=eing:
    if eing % i == 0:
        t+=1
    i+=1

if t==2:
    print(eing, "ist eine Primzahl")
else:
    print(eing, "ist keine Primzahl")
