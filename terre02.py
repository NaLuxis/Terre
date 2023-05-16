############### Afficheur d’arguments ###############

import sys

def main() -> None:
    """Point d'entrée du programme"""
    printed_arguments: None = print_arguments()
    print(printed_arguments)


def print_arguments() -> None:
    """Affiche les arguments passées en ligne de commande"""
    
    list_arguments = sys.argv[1:]
    
    for argument in list_arguments:
        print(argument)
    else:
        exit()


if __name__ == "__main__":
    main()