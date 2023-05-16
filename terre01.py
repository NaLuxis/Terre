############### Nom du programme ###############

import pathlib

def main() -> None:
    """Point d'entée du programme"""
    name_print: None = file_name_print()
    print(name_print)


def file_name_print() -> None:
    """Affiche le nom du ficher"""
    
    path = pathlib.Path(__file__ )

    print(path.name)
    exit()

if __name__ == "__main__":
    main()