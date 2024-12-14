def taille_chaine(T):
    """Calcule la taille de la chaîne de caractères T (sans inclure le caractère de fin de chaîne)."""
    taille = 0
    for c in T:
        if c == '\0':
            break
        taille += 1
    return taille

def pourcentage_voyelles(T):
    """Calcule le pourcentage de voyelles dans la chaîne T."""
    voyelles = 'aeiouyAEIOUY'
    taille = taille_chaine(T)
    if taille == 0:
        return 0
    nb_voyelles = sum(1 for c in T[:taille] if c in voyelles)
    return (nb_voyelles / taille) * 100

def chercher_sous_chaine(T, sous_chaine):
    """Teste si `sous_chaine` est une sous-chaîne de T et retourne la position de la première occurrence."""
    taille_T = taille_chaine(T)
    taille_sous_chaine = len(sous_chaine)
    
    for i in range(taille_T - taille_sous_chaine + 1):
        if T[i:i+taille_sous_chaine] == sous_chaine:
            return i 
    return -1  

def compter_occurrences(T, sous_chaine):
    """Compte le nombre d'occurrences de `sous_chaine` dans T."""
    taille_T = taille_chaine(T)
    taille_sous_chaine = len(sous_chaine)
    
    count = 0
    for i in range(taille_T - taille_sous_chaine + 1):
        if T[i:i+taille_sous_chaine] == sous_chaine:
            count += 1
    return count

if __name__ == "__main__":
    T = list("ceci est un wagon, un joli wagon\0")

    taille = taille_chaine(T)
    print(f"Taille de la chaîne: {taille}")

    pourcentage = pourcentage_voyelles(T)
    print(f"Pourcentage de voyelles: {pourcentage:.2f}%")

    sous_chaine = "wagon"
    position = chercher_sous_chaine(T, sous_chaine)
    if position != -1:
        print(f"La sous-chaîne '{sous_chaine}' est trouvée à la position {position}.")
    else:
        print(f"La sous-chaîne '{sous_chaine}' n'est pas trouvée.")

    occurrences = compter_occurrences(T, sous_chaine)
    print(f"Nombre d'occurrences de la sous-chaîne '{sous_chaine}': {occurrences}")