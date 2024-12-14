import os
from datetime import datetime

def verifier_fichiers():
    fichier1 = input("Entrez le nom du premier fichier : ")
    fichier2 = input("Entrez le nom du deuxième fichier : ")

    if os.path.isfile(fichier1) and os.path.isfile(fichier2):
        taille1 = os.path.getsize(fichier1)
        taille2 = os.path.getsize(fichier2)

        print(f"La taille de '{fichier1}' est de {taille1} octets.")
        print(f"La taille de '{fichier2}' est de {taille2} octets.")

        mtime1 = os.path.getmtime(fichier1)
        mtime2 = os.path.getmtime(fichier2)

        date_modif1 = datetime.fromtimestamp(mtime1)
        date_modif2 = datetime.fromtimestamp(mtime2)

        print(f"La dernière modification de '{fichier1}' : {date_modif1}")
        print(f"La dernière modification de '{fichier2}' : {date_modif2}")

        if mtime1 > mtime2:
            print(f"'{fichier1}' est plus récent que '{fichier2}'.")
        elif mtime1 < mtime2:
            print(f"'{fichier2}' est plus récent que '{fichier1}'.")
        else:
            print("Les deux fichiers ont été modifiés à la même date et heure.")
    else:
        if not os.path.isfile(fichier1):
            print(f"Le fichier '{fichier1}' n'existe pas.")
        if not os.path.isfile(fichier2):
            print(f"Le fichier '{fichier2}' n'existe pas.")

if __name__ == "__main__":
    verifier_fichiers()
