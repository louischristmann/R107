def main():
    personnes = []
    for i in range(2):
        nom = input(f"Entrez le nom de la personne {i + 1} : ").strip()
        prenom = input(f"Entrez le prénom de la personne {i + 1} : ").strip()
        personnes.append((nom.upper(), prenom.capitalize()))

    personnes.sort()

    print("\nRésultats :")
    for nom, prenom in personnes:
        print(f"{prenom} {nom}")

if __name__ == "__main__":
    main()
