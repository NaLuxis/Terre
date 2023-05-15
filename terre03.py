############### L’alphabet à partir de ###############

import sys

def main() -> None:
    """Point d'entrée du programme"""
    valide_letter:str = validate_letter()
    start_letter: str = start_letter_print(valide_letter)
    print(start_letter)


def validate_letter() -> None:
    """Valide s'il n'y a qu'une seule lettre donnée en arguments"""

    if len(sys.argv) != 2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    elif not sys.argv[1].isalpha():
        print("Erreur. Seules des lettres minuscules sont acceptées")
        exit()
    elif not sys.argv[1].islower():
        print("Erreur. Une lettre MINUSCULE est attendues")
        exit()
    else:
        return sys.argv[1]


def start_letter_print(letter_arg: str) -> None:
    """Affiche l'aphabet à partir d'une lettre donnée"""

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    alphabet_lower = [letter.lower() for letter in alphabet]

    index_arg = 0
    for letter in alphabet_lower:
        if letter_arg == letter:
            break
        index_arg += 1

    result = alphabet_lower[index_arg:]

    for letter in result:
        print(letter, end="")
    else:
        print("")
        exit()


if __name__ == "__main__":
    main()