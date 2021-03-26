
#  PAS A JOUR NE FONCTIONNE PAS 
#  PAS A JOUR NE FONCTIONNE PAS 
#  PAS A JOUR NE FONCTIONNE PAS 
#  PAS A JOUR NE FONCTIONNE PAS 


#==============================IMPORTATION DES BIBLIOTHEQUES==============================
import Calcul.dragonManip as cP
from Calcul.buildManip import *
from Calcul.parseurDragonJson import *
#==============================FONCTIONS==============================
#-------------------FONCTION_MANIPULATION_BUILD-----------------------


def selectChamp():
  pass


def affBuild(build):
  print("="*50)

  champDataKey = next(iter(build["champion"]))
  print("Champion : ", build["champion"][champDataKey]["name"], " | level = ", build["champion"]["level"])

  print("\nObjets :")
  itemSet = build["items"]

  for x in itemSet:
    print("->", itemSet[x]["name"])

  print("\nStats : ")
  stats = build["statsTotal"]
  for key, value in stats.items():
    if key == "AS":
      print("AS =", round(stats['AS']['Total'], 3))
    else:
      print(key, "=", round(value))

  print("="*50)


#==============================DEBUT PROGRAMME==============================================

if __name__ == "__main__":

  pathDragon = cP.getDragonName()
  if cP.checkForUpdate() :
    print("Erreur : veulliez mettre à jour le data dragon")
    exit()

  build = {
      "champion": {
          "Aatrox": {
              "name": "Aatrox",
              "stats": {
                      "hp": 580,
                      "hpperlevel": 90,
                      "mp": 0,
                      "mpperlevel": 0,
                      "movespeed": 345,
                      "armor": 38,
                      "armorperlevel": 3.25,
                      "spellblock": 32,
                      "spellblockperlevel": 1.25,
                      "attackrange": 175,
                      "hpregen": 3,
                      "hpregenperlevel": 1,
                      "mpregen": 0,
                      "mpregenperlevel": 0,
                      "crit": 0,
                      "critperlevel": 0,
                      "attackdamage": 60,
                      "attackdamageperlevel": 5,
                      "attackspeedperlevel": 2.5,
                      "attackspeed": 0.651
              },
          },
          "level": 18,
      },
      "items": {},

      "statsTotal": {
          "HP": 0,
          "Mana": 0,
          "Vitesse de deplacement": 0,
          "Armure": 0,
          "Resistance magique": 0,
          "Range": 0,
          "Regen de vie": 0,
          "Regen de mana": 0,
          "Crit chance": 0,
          "AD": 0,
          "AS": {
              "Ratio": 0,
              "Bonus": 0,
              "Total": 0
          },
          "AP": 0,
          "LifeSteal": 0
      },
  }

  if(not(addItem(build))):
      print("Erreur : item introuvable veulliez ressayer")

  calculTotalStats(build)

  affBuild(build)
