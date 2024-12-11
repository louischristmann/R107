def main():
    notes = []
    coefficients = []

    print("Veuillez entrer les notes et coefficients pour 5 modules.")

    for i in range(1, 6):
        entree = input(f"Entrez la note et le coefficient du module {i} (séparés par un espace) : ").strip()
        note, coef = map(float, entree.split())
        notes.append(note)
        coefficients.append(int(coef))

    total_pondere = sum(note * coef for note, coef in zip(notes, coefficients))
    somme_coefficients = sum(coefficients)
    moyenne_generale = total_pondere / somme_coefficients

    est_admis = moyenne_generale > 10 and all(note >= 8 for note in notes)

    print("\nRésultats :")
    print(f"Moyenne générale : {moyenne_generale:.2f}")
    if est_admis:
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")

if __name__ == "__main__":
    main()