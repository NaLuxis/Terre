############### Puissance d’un nombre ###############

import sys

from typing import Dict

def main() -> None:
    """Point d'entrée du programme """
    valide_arg: Dict[str, int] = validate_argument()
    power_result: None = number_power(valide_arg["base"], valide_arg["exposant"])
    print(power_result)


def validate_argument() -> Dict[str, int]:
    """Vérifie qu'il y a 2 nombre, et exposant positif"""

    if len(sys.argv) != 3:
        print(f"Erreur. 2 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    elif not sys.argv[1].lstrip("+-").isdigit() or not sys.argv[2].lstrip("+").isdigit():
        print("Erreur. Deux nombres entier sont attendus, l'exposant ne peut pas être négatif")
        exit()
    return {
        "base": int(sys.argv[1]),
        "exposant": int(sys.argv[2]),
    }


def number_power(base: int, exposant: int) -> None:
    """Calcul la paissance d'une base sur un exposant"""

    print(base ** exposant)
    exit()


if __name__ == "__main__":
    main()
