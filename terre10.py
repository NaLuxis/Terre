############### Nombre premier ###############
#Moins de 8 secondes pour 100 001 029 c'est pas ouf mais ça reste ok

import sys

def main() -> None:
    """Point d'entrée du programme """
    valide_arg: int = validate_arg()
    result: int = prime_number(valide_arg)
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
    elif int(sys.argv[1]) < 2:
        print(f"Erreur. {sys.argv[1]} n'est pas considéré comme un nombre premier")
        exit()
    return int(sys.argv[1])


def prime_number(arg: int) -> str:
    """Calcul si un nombre est premier"""
    for num in range(2,arg + 1):
        if arg % num == 0 and num != arg:
            print(f"Non, {arg} n'est pas un nombre premier")
            exit()
        elif num == arg:
            print(f"Oui, {arg} est un nombre premier.")
            exit()

if __name__ == "__main__":
    main()