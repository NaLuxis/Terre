############### Afficheur d’arguments ###############

import sys

def main() -> None:
    """Point d'entrée du programme"""
    printed_arguments: None = print_arguments()
    print(printed_arguments)


def print_arguments() -> None:
    """Affiche les arguments passées en ligne de commande"""

    if len(sys.argv) < 2:
        print("Erreur. Pour afficher un argument, il faut au moins en donner un")
    
    list_arguments = sys.argv[1:]
    
    for argument in list_arguments:
        print(argument)
    exit()


if __name__ == "__main__":
    main()