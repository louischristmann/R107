def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def verifier_date(date_str):

    if len(date_str) != 8 or not date_str.isdigit():
        print("Erreur : La date doit être une chaîne de 8 chiffres au format jjmmaaaa.")
        return False

    jour = int(date_str[:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:])

    if mois < 1 or mois > 12:
        print(f"Erreur : Le mois ({mois}) doit être entre 01 et 12.")
        return False

    jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if est_bissextile(annee):
        jours_par_mois[2] = 29

    if jour < 1 or jour > jours_par_mois[mois]:
        print(f"Erreur : Le jour ({jour}) n'est pas valide pour le mois {mois} en {annee}.")
        return False

    print(f"La date {date_str} est valide.")
    return True

date_input = input("Entrez une date au format jjmmaaaa : ")
verifier_date(date_input)