a = 0
a = int(a)
b = 0
b = int(b)
c = 0
c = int(c)

for i in range(0, 10):
   x = input()
   x = float(x)
   if x < 10:
     a = a + 1
   else:
    if x >= 10 and x < 15:
       b = b + 1
    else:
      if x >= 15 and x <= 20:
         c = c + 1
      else: print("Une valeur entre 0 et 20")
      x = input()
      x = float(x)
x = 0
print("il y a",a,"valeur entre 0 et 10",b,"valeur entre 10 et 15",c,"valeur entre 15 et 20")