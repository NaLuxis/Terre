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
        print(f"Erreur. 2 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    if sys.argv[1].isdigit():
        print("Erreur. Veuillez entrée une chaîne de caractère")
        exit()
    return sys.argv[1]


def string_return(sting_arg: str) ->str:
    """Retourne la chaîne de caractère donnée"""
    
    return sting_arg[::-1]


if __name__ == "__main__":
    main()