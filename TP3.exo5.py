print("Donnez l'heure de début de la location (un entier) :")
x = input()
x = int(x)
print("Donnez l'heure de fin de la location (un entier) :")
y = input()
y = int(y)
a = 0
a = int(a)
b = 0
b = int(b)
c = 0
c = int(c)

if x > y:
    print("Attention ! Le début de la locatino est après là fin ...")
else:
    if x == y:
        print("Attention ! l'heure de fin est identique à l'heure de début.")
    else:
        if x > 24 or x < 0 or y > 24 or y < 0:
            print("Les heures doivent être comprises entre 0 et 24 !")
        else:
            print("Vous avez loué votre vélo pendant")
            for i in range(x,y):
                if i < 7:
                   a = a + 1
                else:
                    if i >= 7 and i < 17:
                        b = b + 1
                    else:
                        a = a + 1


c = a + b * 2
if a > 0:
    print(a,"heure(s) au tarif horaires de 1.0 euro(s)")
else:
    print()
if b > 0:
    print(b,"heure(s) au tarif horaires de 2.0 euro(s)")
else:
    print()
print("Le montant total à payer est de ",c," euro (s).")