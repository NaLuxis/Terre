############### Divisions ###############

import sys
from typing import Dict

def main() -> None:
    """Point d'entée du programme"""
    valide_arg: Dict[str, int] = validate_argument()
    print_division: str = division(valide_arg["dividend"], valide_arg["divisor"])
    print(valide_arg)


def validate_argument() -> Dict[str, int]:
    """Valide que 2 nombre entier sont passés en arguments"""

    if len(sys.argv) != 3:
        print(f"Erreur. 2 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    elif not sys.argv[1].lstrip("-+").isdigit() and not sys.argv[2].lstrip("-+").isdigit():
        print("Erreur. 2 nombres entiers sont attendus")
        exit()
    else:
        return {
            "dividend": int(sys.argv[1]),
            "divisor": int(sys.argv[2]),
        }



def division(dividend, divisor):
    """Fait une division et affiche le résultat plus le reste"""

    if divisor == 0:
        print("Erreur. La division par 0 n'est pas possible")
        exit()
    elif divisor > dividend:
        print("Erreur. Le diviseur doit être plus petit que le dividende")
        exit()
    else:
        quotient = dividend / divisor
        remainder = dividend % divisor
        print(f"Résultat : {int(quotient)}")
        print(f"Reste : {remainder}")
        exit()



if __name__ == "__main__":
    main()