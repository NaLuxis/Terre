############### L’alphabet à partir de ###############

import sys

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

letterArgument = [letter.lower() for letter in sys.argv[1]]

for letter in alphabet:
    print(letter.lower(), end="")
else:
    print("")

#pour l'instant je print tout l'alphabet en minuscule quand je passe une lettre en argument
#je transforme l'argument en lower pour gérer les erreur de saisies 
#dans le cas ou je met pas de lettre j'ai une erreur donc c'est cool (a voir pour faire une erreur perso)
