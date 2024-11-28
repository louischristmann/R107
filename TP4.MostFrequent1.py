L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

def trouver_nombre_frequent(liste):
    most = {}
    
    for nombre in liste:
        if nombre in most:
            most[nombre] += 1
        else:
            most[nombre] = 1
    
    max_most = 0
    nombre_frequent = None
    
    for nombre in liste: 
        if most[nombre] > max_most:
            max_most = most[nombre]
            nombre_frequent = nombre
    
    print(f"Le nombre le plus frequent dans la liste est le : {nombre_frequent} ({max_most} x)")

trouver_nombre_frequent(L1)