############### Pair ou impair ###############

#récupérer les arguments
#s'asurer qu'il y en ai le bon nombre
#s'asurer qu'il soit du bon type
#si j'ia un argument valide je dit s'il et pair ou impair

import sys

search_number = sys.argv
search_type = search_number[1]

if len(search_number) < 2:
    print("Tu ne me la mettras pas à l'envers")
elif len(search_number) > 2:
    print("Tu ne me la mettras pas à l'envers")
else:
    pass


def even_odd(number):
    if number % 2 == 0:
        print("pair")
    else:
        print("impair")

if int(search_type):
    print(even_odd(int(search_number)))