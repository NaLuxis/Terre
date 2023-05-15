############### L’alphabet ###############

def main() -> None:
    """Point d'entrée du programme"""
    printed_alphabet: str = print_alphabet()
    print(printed_alphabet)


def print_alphabet() -> None:
    """Affiche l'alphabet entier en minuscules"""
    
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for letter in alphabet:
        print(letter.lower(), end="")
    else:
        print("")
        exit()


if __name__ == "__main__":
    main()
    exit()