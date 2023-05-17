############### Nombre premier ###############

import sys

def main() -> None:
    """Point d'entrée du programme """
    valide_arg: int = validate_arg()
    result: None = prime_number(valide_arg)
    print(result)


def validate_arg() -> int:
    """Vérifie qu'il n'y a qu'un nombre positif qui est donné"""

    if len(sys.argv) != 2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    elif not sys.argv[1].lstrip("+").isdigit():
        print("Erreur. Seuls les nombres entiers positifs sont acceptés")
        exit()
    elif int(sys.argv[1]) < 2:
        print(f"Erreur. {sys.argv[1]} n'est pas considéré comme un nombre premier")
        exit()
    return int(sys.argv[1])


def prime_number(arg: int) -> None:
    """Calcul si un nombre est premier"""

    for num in range(2,arg + 1):
        if arg % num == 0 and num != arg:
            print(f"Non, {arg} n'est pas un nombre premier")
            exit()
        elif num == arg:
            print(f"Oui, {arg} est un nombre premier")
            exit()


if __name__ == "__main__":
    main()