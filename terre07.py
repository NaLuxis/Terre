############### Taille d’une chaîne ###############

import sys

def main() -> None:
    """Point d'entrée du programme """
    arg: str = strig_validate()
    length_result: None = string_length(arg)
    print(length_result)


def strig_validate() -> str:
    """Regarde si l'argument est valide"""

    if len(sys.argv) !=2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    if sys.argv[1].isdigit():
        print("Erreur. Veuillez entrée une chaîne de caractère")
        exit()
    return sys.argv[1]


def string_length(string_arg: str) -> None:
    """Compte le nombre de caractères dans une chaine de caractères donnée en paramètre"""

    print(len(string_arg))
    exit()


if __name__ == "__main__":
    main()