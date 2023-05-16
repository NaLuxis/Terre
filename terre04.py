############### Pair ou impair ###############

import sys

def main() -> None:
    """Point d'entrée du programme"""
    valide_arg:int = validate_argument()
    even_odd_print: int = even_odd(valide_arg)
    print(even_odd_print)


def validate_argument() -> int:
    """Valide si un integer et donnée en argument"""

    if len(sys.argv) != 2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    elif not sys.argv[1].lstrip("-+").isdigit():
        print("Erreur. Un nombre entier est attendu")
        exit()
    else:
        return int(sys.argv[1])

    
def even_odd(int_arg: int) -> str:
    """Affiche si un integer donné est pair ou impair"""

    if int_arg % 2 == 0:
        print("Pair")
        exit()
    else:
        print("Impair")
        exit()

if __name__ == "__main__":
    main()