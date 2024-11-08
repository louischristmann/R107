import time
print("entrer un entier postif")
x = input()
x = int(x)
if x <= 0:
    print("Un entier positif")
    x = input()
    x = int(x)
else:
    for i in range(x, -1, -1):
        print(i)
        time.sleep(1)