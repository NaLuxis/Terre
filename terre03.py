############### L’alphabet à partir de ###############

import sys

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

letterArgument = sys.argv[1]

alphabetLower = [letter.lower() for letter in alphabet]

indexArgument = 0
for letter in alphabetLower:
    if letterArgument == letter:
        break
    indexArgument += 1
        


print(indexArgument)