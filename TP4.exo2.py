nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0

notes = []

for i in range(nombreEtudiants):
    while True:
        try:
            note = float(input(f"Note etudiant {i} : "))
            if 0 <= note <= 20:
                notes.append(note)
                break
            else:
                print("La note doit être comprise entre 0 et 20.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

sommeNotes = sum(notes)
moyenne = sommeNotes / nombreEtudiants

print(f"Moyenne de classe : {moyenne:.2f}")
print("Numéro de l’Etudiant | note | ecart a la moyenne")

for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]:.2f} | {ecart:.2f}")
