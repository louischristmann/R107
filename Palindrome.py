def main():
    chaine = input("Entrez un mot ou une phrase : ").strip()

    chaine_epuree = "".join(c.lower() for c in chaine if c.isalpha())

    if chaine_epuree == chaine_epuree[::-1]:
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

if __name__ == "__main__":
    main()