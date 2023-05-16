############### Terre : ok ###############

import random

def main() -> None:
    """Point d'entée du programme"""
    random: None = random_adjectives()
    print(random)


def random_adjectives() -> None:
    """Affiche : J'ai terminé l'Épreuve de la Terre et c'était [un adjectif random] """

    list_adjctives = ["sans difficulté", "simple", "aisé", "facile", "commode", "élémentaire", "enfantin",
                      "simple", "marrant", "drôle", "amusant", "divertissant", "rigolo", "distrayant",
                       "à l'aise", "instructeur", "éducateur", "formateur", "pédagogue", "cool",
                       "beaucoup de boulot", "de la recherche", "du travail", "bien"]

    random_item = random.randint(1, len(list_adjctives))
    print(f"J'ai terminé l'Épreuve de la Terre et c'était {list_adjctives[random_item]}")
    exit()


if __name__ == "__main__":
    main()