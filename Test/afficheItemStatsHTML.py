
#  PAS A JOUR NE FONCTIONNE PAS 
#  PAS A JOUR NE FONCTIONNE PAS 
#  PAS A JOUR NE FONCTIONNE PAS 
#  PAS A JOUR NE FONCTIONNE PAS 


#==============================IMPORTATION DES BIBLIOTHEQUES==============================
import json
import os
from dataDragonCheck import getDragonName

#Annexe c'est pour faire jolie
from bs4 import BeautifulSoup
import tempfile
import webbrowser
#==============================FONCTIONS==============================





#==============================DEBUT PROGRAMME==============================================
pathDragon = getDragonName()
if(pathDragon == ""):
  print("veulliez mettre à jour votre Parseur")
  exit()

itemTarget = input("Entrez le nom de l'item dont vous voulez la description :")
pathItem = os.path.dirname(__file__) + "/" + pathDragon + "/" + pathDragon[11:] + "/data/fr_FR/item.json"

with open(pathItem,"r") as itemsFile:
  itemsData = itemsFile.read()
dragon = json.loads(itemsData)

for x in dragon["data"]:
  if(itemTarget == dragon["data"][x]["name"]):
    #Affiche la description écrite en html de l'item dans le navigateur par défaut
    descri = dragon["data"][x]["description"]
    soup = BeautifulSoup(descri, features="lxml")

    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
        url = 'file://' + f.name
        f.write(soup.prettify())
    webbrowser.open(url)

    #Affiche le contenue brut en Json de l'item
    #print( json.dumps(dragon["data"][x], indent=4)) 
    exit()

print("item non connue")
