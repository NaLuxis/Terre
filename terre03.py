############### L’alphabet à partir de ###############

import sys

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

letter_argument = sys.argv[1]

alphabet_lower = [letter.lower() for letter in alphabet]

index_argument = 0
for letter in alphabet_lower:
    if letter_argument == letter:
        break
    index_argument += 1

result = alphabet_lower[index_argument:]

for letter in result:
    print(letter, end="")
else:
    print("")

    

        


