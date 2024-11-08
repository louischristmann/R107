import random
x = random.randrange(0, 100, 1)
print("essayer de deviner le nombre mystère")
a = input()
a = int(a)
b = 0
b = int(b)
while a > x and a < x:
    b = b + 1
    if a > x:
        print("Le nombre mystère est plus petit")
    else:
        if a < x:
            print("le nombre mystère est plus")
        else:
            print("bravo, tu as trouver le nombre mystère")
    print("tu a pris",b,"tentavive(s) pour trouver le nombre")