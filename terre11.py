############### 24 to 12 ###############

import sys

def main() -> None:
    """Point d'entrée du programme"""
    valide_time: str = validate_time()
    converted_time: str = convert_time(valide_time)
    print(valide_time)


def validate_time() -> str:
    """Valide ou non si l'argument est une heure au bon format"""
    time = sys.argv[1].split(":")
    hour = time[0]
    minute = time[1]
    
    if len(sys.argv) != 2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()
    elif not hour.isdigit() or not minute.isdigit():
        print("Erreur dans la saisie. Une heure avec ce format est attendue : XX:XX")
        exit()
    elif len(hour) !=2 or len(minute) != 2:
        print("Erreur dans la saisie. Saisis attendue : XX:XX")
        exit()
    elif len(hour) == 2 and len(minute) == 2:
        hour_template = f"{hour:02}:{minute:02}" 
        return hour_template, hour, minute


def convert_time(time: str) -> str:
    """Convertie une heure en format 24h vers 12h"""


if __name__ == "__main__":
    main()

# Si l'heure est entre 00:00 et 09:59 je retire le 0 initial et ajoute AM
# Si l'heure est entre 10:00 et 11:59 j'ajoute juste AM
# Si l'heure est entre 12:00 et 12:59 j'ajoute juste PM
# Si l'heure est entre 13:00 et 23:59 j'enlève 12 heures et ajoute PM
# Si l'heure est 00:00 elle est égale à 12:00 AM

# les heures ne peuvent pas êtres plus grande que 24
# les minutes ne peuvent pas êtres plus grande que 60

# J'afiche la même heure au format 12 heures : 1:50PM 