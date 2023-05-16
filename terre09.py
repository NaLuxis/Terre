############### Racine carrée d’un nombre ###############

import sys

def main() -> None:
    """Point d'entrée du programme """
    valide_arg: int = validate_arg()
    result: None = sqrt(valide_arg)
    print(result)


def validate_arg() -> int:
    """Vérifie qu'il n'y a qu'un nombre positif qui est donné"""

    if len(sys.argv) != 2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    elif not sys.argv[1].lstrip("+").isdigit():
        print("Erreur. Seuls les nombres entiers positifs sont acceptés")
        exit()
    return int(sys.argv[1])


def sqrt(arg: int) -> None:
    """Cacul de la racine carrée d'un nombre"""

    print(arg ** 0.5)
    exit()


if __name__ == "__main__":
    main()