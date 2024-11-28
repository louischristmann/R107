nMax = 10

v1 = []
v2 = []

while True:
    try:
        n = int(input(f"Entrez la taille des vecteurs (1 à {nMax}): "))
        if 1 <= n <= nMax:
            break
        else:
            print(f"La taille doit être entre 1 et {nMax}.")
    except ValueError:
        print("Veuillez entrer un entier valide.")

print("Entrez les composantes du premier vecteur (v1) :")
for i in range(n):
    while True:
        try:
            val = int(input(f"v1[{i}] = "))
            v1.append(val)
            break
        except ValueError:
            print("Veuillez entrer un entier valide.")

print("Entrez les composantes du deuxième vecteur (v2) :")
for i in range(n):
    while True:
        try:
            val = int(input(f"v2[{i}] = "))
            v2.append(val)
            break
        except ValueError:
            print("Veuillez entrer un entier valide.")

produit_scalaire = sum(v1[i] * v2[i] for i in range(n))

print(f"Le produit scalaire des vecteurs v1 et v2 est : {produit_scalaire}")