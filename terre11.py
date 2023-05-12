############### 24 to 12 ###############

import sys
from typing import Dict

def main() -> None:
    """Point d'entrée du programme"""
    valide_time: Dict[str, str] = validate_time()
    converted_time: str = convert_time(valide_time["hour"], valide_time["minute"])
    print(converted_time)


def validate_time() -> Dict[str,str]:
    """Valide ou non si l'argument est une heure au format attedus"""
    
    if len(sys.argv) != 2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()

    time = sys.argv[1].split(":")
    hour = time[0]
    minute = time[1]

    if not hour.isdigit() or not minute.isdigit():
        print("Erreur dans la saisie. Une heure avec ce format est attendue : XX:XX")
        exit()
    elif len(hour) !=2 or len(minute) != 2:
        print("Erreur dans la saisie. Saisis attendue : XX:XX")
        exit()
    elif int(hour) > 23:
        print("Erreur, les heures ne peuvent pas dépasser 23")
        exit()
    elif int(minute) > 59:
        print("Erreur, une minutes ne peuvent pas dépasser 59")
        exit()
    elif len(hour) == 2 and len(minute) == 2:
        return {
            "hour": hour,
            "minute": minute,
        }


def convert_time(hour: str, minute: str) -> str:
    """Convertie une heure en format 24h vers 12h"""
    if int(hour) == 00 and int(minute) == 00:
        print("12:00 a.m")
        exit()
    elif int(hour) < 10:
        print(f"{hour[1]}:{minute} a.m")
        exit()
    elif int(hour) == 10 or int(hour) == 11:
        print(f"{hour}:{minute} a.m")
        exit()
    elif int(hour) == 12:
        print(f"{hour}:{minute} p.m")
        exit()
    elif int(hour) >= 13:
        print(f"{int(hour) - 12}:{minute} p.m")
        exit()

if __name__ == "__main__":
    main()