############### Racine carrée d’un nombre ###############

# Le nombre doit être entier et positif
# Je calcul sa racine carré
# J'afiche le résultat

import sys

def main() -> None:
    """Point d'entrée du programme """
    valide_arg: int = validate_arg()
    result: int = sqrt(valide_arg)
    print(result)


def validate_arg() -> int:
    """Vérifie qu'il n'y a qu'un nombre positif qui est donné"""
    if len(sys.argv) != 2:
        print(f"Erreur, le nombres d'arguments entré(s) ({len(sys.argv) - 1}) est incorect. Nombre attendus : 1")
        exit()
    elif sys.argv[1].isdecimal() != True:
        if sys.argv[1].count("+"):
            pass
        elif sys.argv[1].count("-"):
            print("Erreur. Seuls les nombres positifs sont acceptés")
            exit()
        else:
            print("Erreur. Un nombre entier est attendus")
            exit()
    return int(sys.argv[1])


def sqrt(arg: int) -> int:
    """Cacul de la racine carrée d'un nombre"""
    return arg ** 0.5


if __name__ == "__main__":
    main()