import random
nombre_aleatoire = random.randint(0, 100)
if nombre_aleatoire < 50:
    print("Pile!")
else:
    print("Face!")