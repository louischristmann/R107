n = int(input("donnez la taille de la liste de nombre :"))
liste = []
j = 0

for i in range(0,n):
    x = int(input("donnez les nombres de la liste un par un"))
    liste.append(x)

for i in range(0,len(liste)):
    for p in range(i,len(liste)):
        if liste[p] < liste[i]:
            a = liste[p]
            liste[p] = liste [i]
            liste[i] = a
        else:
            j = 0        
liste.sort()
print(liste)

#affiche le même resultat que l'exercice6_2 mais en 2 lignes de code au lieu d'une