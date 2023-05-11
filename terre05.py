############### Divisions ###############

#je récupère les 2 nombres OK
#je défini de 1er nombre et le deuxième au bon endroit OK
#La division par 0 n'est pas possible OK
#diviser un nombre par un nombre plus grand n'est pas possible OK

#j'ai une fonction qui prendra les deux nombres et fait le calcul
#la fonction arrondie le résultat 
#elle retour le reste

#j'ai un print pour le rétultat
#j'ai un print pour le reste

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