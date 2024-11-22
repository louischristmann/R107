print("entrer 1 pour une boucle pour, 2 pour une boucle tant que :")
x = input()
x = int(x)

print("entrez un nombre")
n = input()
n = int(n)
a = 0
a = int(a)
b = 1
b = int(b)

while x > 2:
    if x == 1:
        for i in range(n,0,-1):
            a = i
            b = b * a
        print(b)

else :
    if x == 2:
        while n > 0 :
            a = n
            b = b * a
            n = n - 1
        print(b)
    else:
        print("entrer 1 pour une boucle pour, 2 pour une boucle tant que:")
        x = input()