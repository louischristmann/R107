# Fonction pour décomposer une somme en billets et pièces
def decomposer_somme(somme):
    billets_et_pieces = [100, 50, 10, 2, 1]  # Liste des valeurs de billets et pièces disponibles
    resultat = {}  # Dictionnaire pour stocker la décomposition

    for valeur in billets_et_pieces:
        resultat[valeur], somme = divmod(somme, valeur)  # Utilisation de divmod pour calculer le nombre et le reste

    return resultat

somme = int(input("Entrez une somme en euros : "))

resultat = decomposer_somme(somme)

def afficher_resultat(somme, resultat):
    print(f"{somme} euros, c'est donc :")
    print(f"  {resultat[100]} billets de 100,")
    print(f"  {resultat[50]} billets de 50,")
    print(f"  {resultat[10]} billets de 10,")
    print(f"  {resultat[2]} pièces de 2,")
    print(f"  {resultat[1]} pièce de 1.")

afficher_resultat(somme, resultat)
