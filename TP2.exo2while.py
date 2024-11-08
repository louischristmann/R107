import time
print("entrer un entier postif")
x = input()
x = int(x)
a = x
if x <= 0:
    print("Un entier positif")
    x = input()
    x = int(x)
else:
    while a >= 0:
        print(a)
        a = a - 1
        time.sleep(1)