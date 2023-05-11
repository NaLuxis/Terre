############### Inverser une chaîne ###############
#prend pas en charge le type de donnée que j'entre car je no trouve pas de moyen de le récupérer

import sys

def main() -> None:
    """Point d'entrée du programme """
    arg: str = strig_argument()
    string_returned: str = string_return(f"{arg}")
    print(string_returned)


def strig_argument() -> str:
    """Regarde si l'argument et valide"""
    if len(sys.argv) !=2:
        print("Erreur, veuillez entrée une seule chaîne de caractère")
        exit()
    if sys.argv[1].isnumeric():
        print("Erreur, veuillez entrée une seule chaîne de caractère")
        exit()
    return sys.argv[1]


def string_return(sting_arg: str) ->str:
    """Retourne la chaîne de caractère donnée"""
    return sting_arg[::-1]


if __name__ == "__main__":
    main()