############### Inverser une chaîne ###############

import sys

def main() -> None:
    """Point d'entrée du programme """
    arg: str = strig_validate()
    string_returned: str = string_return(arg)
    print(string_returned)


def strig_validate() -> str:
    """Valide si l'argument est une chaîne de caractère"""

    if len(sys.argv) !=2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    if sys.argv[1].lstrip(".").isdigit():
        print("Erreur. Veuillez entrée une chaîne de caractère")
        exit()
    return sys.argv[1]


def string_return(sting_arg: str) -> str:
    """Affiche à l'envers la chaîne de caractère donnée"""
    
    print(sting_arg[::-1])
    exit()


if __name__ == "__main__":
    main()