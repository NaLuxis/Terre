############### Trié ou pas ###############

import sys
from typing import List

def main() -> None:
    """Point d'entée du programme"""
    valide_args: List[int] = validate_arguments()
    sorted_list: None = sort_or_not(valide_args)
    print(sorted_list)


def validate_arguments() -> List[int]:
    """Valide si les arguments donnés correspondes à une list d'entiers"""

    if len(sys.argv) < 3:
        print(f"Erreur. 2 arguments attenduts au minimum, vous en avez donné : {len(sys.argv) - 1}")
        exit()

    numbers_list = []

    for numbers in sys.argv[1:]:
        if not numbers.lstrip("-+").isdigit():
            print("Seulement des nombres entiers sont attendus")
            exit()
        else:
            numbers_list.append(int(numbers))
    
    return numbers_list


def sort_or_not(numbers_list: List[int]) -> None:
    """Affiche si une liste d'entier est trier ou non et dans quel ordre"""
    
    copy_numbers_list = numbers_list.copy()

    ascending_list = sorted(copy_numbers_list)
    descending_list = sorted(copy_numbers_list, reverse = True)

    if numbers_list == ascending_list:
        print("La liste est triée dans l'ordre croissant")
        exit()
    elif numbers_list == descending_list:
        print("La liste est triée dans l'ordre décroissant")
        exit()
    else:
        print("La liste n'est pas triée")
        exit()

if __name__ == "__main__":
    main()