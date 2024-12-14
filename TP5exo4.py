def decomposer_somme(somme):
    valeurs = [100, 50, 10, 2, 1]
    decomposition = {}

    for valeur in valeurs:
        decomposition[valeur] = somme // valeur
        somme %= valeur

    return decomposition

try:
    somme = int(input("Entrez une somme d'argent en euros : "))
    if somme < 0:
        print("Veuillez entrer une somme positive.")
    else:
        resultat = decomposer_somme(somme)

        print(f"{somme} euros, c'est donc {resultat[100]} billets de 100, {resultat[50]} de 50, {resultat[10]} de 10, {resultat[2]} pièces de 2 et {resultat[1]} pièce de 1.")
except ValueError:
    print("Veuillez entrer un nombre entier valide.")

