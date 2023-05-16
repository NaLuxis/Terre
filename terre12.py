############### 12 to 24 ###############

import sys
from typing import Dict

def main() -> None:
    """Point d'entrée du programme"""
    valide_time: Dict[str, str] = validate_time()
    converted_time: None = convert_time(valide_time["hour"], valide_time["minute"], valide_time["AM_PM"])
    print(converted_time)


def validate_time() -> Dict[str,str]:
    """Valide ou non si l'argument est une heure au format attedus"""

    if len(sys.argv) != 2:
        print(f"Erreur. 1 argument attendut, vous en avez donné : {len(sys.argv) - 1}")
        exit()

    if sys.argv[1].count(":") and (sys.argv[1].upper().count("AM") or sys.argv[1].upper().count("PM")):
        time = sys.argv[1].split(":")
        hour = time[0]
        minute = time[1][0:2]
        ante_post = time[1][2:].upper()
    else:
        print("Erreur dans la saisie. Une heure avec ce format est attendue : X:XX ou XX:XX | AM ou PM min & maj")
        exit()

    if not hour.isdigit() or not minute.isdigit():
        print("Erreur dans la saisie. Une heure avec ce format est attendue : X:XX ou XX:XX | AM ou PM min & maj")
        exit()
    elif len(hour) > 2 or len(minute) != 2 or len(ante_post) != 2:
        print("Erreur dans la saisie. Saisis attendue : X:XX ou XX:XX | AM ou PM min & maj")
        exit()
    elif int(hour) > 12:
        print("Erreur, les heures ne peuvent pas dépasser 12")
        exit()
    elif int(hour) == 0:
        print("Erreur, une heure ne peut pas être égale à 0")
        exit()
    elif int(minute) > 59:
        print("Erreur, les minutes ne peuvent pas dépasser 59")
        exit()
    else:
        return {
            "hour": hour,
            "minute": minute,
            "AM_PM": ante_post,
        }

def convert_time(hour: str, minute: str, meridiem: str) -> None:
    """Convertie une heure en format 12h vers 24h"""

    if meridiem == "AM":
        if int(hour) == 12:
            print(f"00:{minute}")
            exit()
        elif int(hour) < 10:
            print(f"0{hour}:{minute}")
            exit()
        elif int(hour) < 12:
            print(f"{hour}:{minute}")
            exit()
    elif meridiem == "PM":
        if int(hour) == 12:
            print(f"{hour}:{minute}")
            exit()
        elif int(hour) < 12:
            print(f"{int(hour) + 12}:{minute}")
            exit()
        
    

if __name__ == "__main__":
    main()
