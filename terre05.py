############### Divisions ###############

import sys

dividend = int(sys.argv[1])
divisor = int(sys.argv[2])

def division(a, b):
    print(f"résultat : {int(a / b)}")
    print(f"reste : {int(a % b)}")

if divisor == 0:
    print("erreur.")
elif divisor > dividend:
    print("erreur.")
else:
    division(dividend, divisor)