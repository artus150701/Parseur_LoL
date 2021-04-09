import json
import os
from Calcul.dragonManip import getDragonName

def getChamp(pathDragon, build, dictChamp):
  dataChamps = {}

  champTarget = input("Entrez le nom du champion :")

  lvlChamp = int (input("Entrez le niveau de votre champion :"))
  while (19 < lvlChamp or lvlChamp < 0):
    lvlChamp = int(input("Entrez un niveau valide ou entre 1 et 18 :"))
  
  pathChamp = os.path.dirname(__file__) +"/" + pathDragon + "/" + pathDragon[11:] + "/data/fr_FR/champion.json"

  with open(pathChamp, "r") as champFile:
    champData = champFile.read()
    dragon = json.loads(champData)
    dataChamps = dragon.get("data")
    dictChamp = dataChamps.get(champTarget)
    build = {"champion": { champTarget : { "name" : dictChamp.get("name"), "stats" : dictChamp.get("stats"), "level": lvlChamp, "items": {},"statsTotal": {"HP": 0,"Mana": 0,"Vitesse de deplacement": 0,"Armure": 0,"Resistance magique": 0,"Range": 0,"Regen de vie": 0,"Regen de mana": 0,"Crit chance": 0, "AD": 0,"AS": { "Ratio": 0, "Bonus": 0,  "Total": 0},"AP": 0,"LifeSteal": 0}}}}
    print(dictChamp)
    print(build)

pathDragon = getDragonName()
if(pathDragon == ""):
  print("Erreur : veuillez mettre à jour votre Parseur")
  exit()

build = {}
dictChamp = {}
getChamp("dragontail-11.6.1", build, dictChamp)

