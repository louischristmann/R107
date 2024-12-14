eh = int(input("Indiquer votre salaire horaire : "))
h = int(input("Indiquer maintenant le nombre de de travaille : "))
s = eh * h

if h > 160:
    h = h - 160
    s = s + eh * h * 1.25
    if h < 40:
        h = h - 40
        s = s + eh * h * 1.5

print("Vous avez gagner ",s," euros")