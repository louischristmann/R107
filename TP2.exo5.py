a = int(input("Entrer un nombre entier:"))
if a > 0:
  if a%2 == 0:
    print("Le nombre est postif et pair")
  else: print("Le nombre est positif et impair")
else: 
  if a < 0:
    if a%2 == 0:
      print("Le nombre est négatif et pair")
    else: print("Le nombre est négatif et impair")
if a == 0:
  print("Le nombre est zéro (et il est pair)")