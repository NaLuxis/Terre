############### Puissance d’un nombre ###############

import sys

from typing import Dict

def main() -> None:
    """Point d'entrée du programme """
    valide_arg: Dict[str, int] = validate_argument()
    power_result: int = number_power(valide_arg["base"], valide_arg["exposant"])
    print(power_result)


def validate_argument() -> Dict[str, int]:
    """Vérifie qu'il y a 2 nombre, et exposant positif"""
    if len(sys.argv) != 3:
        print(f"Erreur, le nombres d'arguments entré(s) ({len(sys.argv) - 1}) est incorect. Nombre attendu : 2")
        exit()
    elif (sys.argv[1].isdigit() and sys.argv[2].isdigit()) != True:
        if sys.argv[2] < "0" and sys.argv[2].count("+") != True:
            print("Les exposants négatifs ne sont pas admis")
            exit()
        else:
            if sys.argv[2].count("+"):
                pass
            elif sys.argv[1].count("-"):
                pass
            else:
                print("2 nombre sont attendus")
                exit()
    return {
        "base": int(sys.argv[1]),
        "exposant": int(sys.argv[2]),
    }


def number_power(base: int, exposant: int):
    """Calcul la paissance d'une base sur un exposant"""
    return base ** exposant


if __name__ == "__main__":
    main()
