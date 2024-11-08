x = int(input("entrer la valeur"))
a = 0
a = int(a)
b = 0
b = int(b)
while b < x:
    a = a + 1
    b = a + b
    if b > x:
       a = a - 1
    else: 
        print(a)