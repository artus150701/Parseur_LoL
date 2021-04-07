import Calcul.parseurDragonJson as parseurDragon
import pprint

listItem = parseurDragon.lisItem()

pprint.pprint(listItem)

print("nombre d'items dans le jeu = ",len(listItem))