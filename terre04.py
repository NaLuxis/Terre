############### Pair ou impair ###############

#après 7 heures de code j'ai réussi OUIIIIII, je suis trop content ^^

import sys

search_number = sys.argv

if len(search_number) < 2:
    print("Tu ne me la mettras pas à l'envers")
elif len(search_number) > 2:
    print("Tu ne me la mettras pas à l'envers")
else:
    count = 0
    for chart in range(0,10):
        is_int = search_number[1].count(f"{count}")
        count = count + 1
        if is_int > 0:
            if int(search_number[1]) % 2 == 0:
                print("pair")
            else:
                print("impair")
            break
    else:
        print("Tu ne me la mettras pas à l'envers")