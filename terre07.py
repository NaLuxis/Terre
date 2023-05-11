############### Taille d’une chaîne ###############

import sys

def main() -> None:
    """Point d'entrée du programme """
    arg: str = strig_validate()
    length_result: int = string_length(arg)
    print(length_result)


def strig_validate() -> str:
    """Regarde si l'argument est valide"""
    if len(sys.argv) !=2:
        print("erreur.")
        exit()
    if sys.argv[1].isnumeric():
        print("erreur.")
        exit()
    return sys.argv[1]


def string_length(string_arg: str) -> int:
    """Compte le nombre de caractères dans une chaine de caractères donnée en paramètre"""
    return len(string_arg)


if __name__ == "__main__":
    main()