############### Nom du programme ###############

import pathlib

fileName = __file__ 
p = pathlib.Path(fileName)

print(p.name)