############### Trouver la Suisse (lol) ###############

import sys
from typing import Dict

def main() -> None:
    """Point d'entrée du programme"""
    valide_args: Dict[str, int] = validate_arguments()
    sorted_value: None = search_mid_value(valide_args["first"], valide_args["second"], valide_args["third"])
    print(sorted_value)


def validate_arguments() -> Dict[str, int]:
    """Valide si 3 entier sont donnés"""

    if len(sys.argv) != 4:
        print(f"Erreur. 3 arguments attenduts, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    else:
        first = sys.argv[1]
        second = sys.argv[2]
        third = sys.argv[3]
    
    if not first.lstrip("-+").isdigit() or not second.lstrip("-+").isdigit() or not third.lstrip("-+").isdigit():
        print("Erreur. Les 3 arguments doivent êtres des nombres entiers")
        exit()
    elif first == second or first == third or second == third or first == second == third:
        print("Erreur. Pour trouver l'entier du millieu il en faut 3 différents")
        exit()
    else:
        return {
            "first": int(first),
            "second": int(second),
            "third": int(third),
        }


def search_mid_value(first: int, second: int, third: int) -> None:
    """Avec 3 entier donnés, cherche la valeur du millieu"""
    
    not_sort = [first, second, third]
    sort_list = sorted(not_sort)
    print(sort_list[1])
    exit()


if __name__ == "__main__":
    main()