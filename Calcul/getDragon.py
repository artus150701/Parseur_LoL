import json
import os
from . import dragonManip

""" 
attention ces items ne sont pas sensé être dans un build et sont pourtant dans item.json
3364 trinket rouge
3400 gangplank passif
3363 trinket bleue
3340 trinket jaune
3330 fiddle passiv
3599 et 3600 kalista passiv
3513 herald
2052 poro cookies
"""

# ============== Parse les fichiers json en dico  ==========
def getItemsData():
  dragonPath = dragonManip.getDragonPath()
  dragonName = dragonManip.getDragonName()
  pathItem = os.path.join(dragonPath, dragonName[11:], "data", "fr_FR", "item.json")
  with open(pathItem, "r") as itemsFile:
    itemsJson = itemsFile.read()
  itemData = json.loads(itemsJson)

  #Suppression des objets non achetable
  del itemData["data"]["3364"] #trinket rouge
  del itemData["data"]["3363"] #trinket bleue
  del itemData["data"]["3340"] #trinket jaune
  del itemData["data"]["3330"] #fiddle lanterne
  del itemData["data"]["3599"] #kalista
  del itemData["data"]["3600"] #kalista
  del itemData["data"]["3513"] #herald
  del itemData["data"]["3400"] #gp serpent
  del itemData["data"]["2052"] #poro biscuit
  del itemData["data"]["2010"] #cookies
  del itemData["data"]["2419"] #chronometre rune
  del itemData["data"]["2421"] #chrono cassé
  del itemData["data"]["2424"] #autre chrono cassé
  del itemData["data"]["2423"] #chrono parfait
  
  return  itemData

def getChampionData():
  dragonPath = dragonManip.getDragonPath()
  dragonName = dragonManip.getDragonName()
  pathChampion = os.path.join(dragonPath, dragonName[11:], "data", "fr_FR", "champion.json")
  with open(pathChampion, "r") as championFile:
    championJson = championFile.read()
  return json.loads(championJson)

# ============= recuperation precise de donnee depuis les dicos de json

#Cette fonction marche qu'avec le nom de l'item en argument
def getOneItemData(itemId):
  dataItems = getItemsData()
  return dataItems["data"][itemId]
  """
  for x in dataItems["data"]:
    if(itemName == dataItems["data"][x]["name"]):
      return dataItems["data"][x]

  return False
  """
  
  
def getOneChampData(champName):
  dataChamp = getChampionData()
  dictChamp = (dataChamp.get("data")).get(champName)
  return {dictChamp.get("id") : {"name": dictChamp.get("name"), "stats": dictChamp.get("stats")}}
  
  

def getLisItemId():
  itemsData = getItemsData()

  listItemId = []
  for id in itemsData["data"]:
    listItemId.append(id)
  return listItemId

def getListChampionId():
  championData = getChampionData()

  listChampionId = []
  for id in championData["data"]:
    listChampionId.append(id)
  return listChampionId

def getIconChampPath(champId):
  dragonPath = dragonManip.getDragonPath()
  return os.path.join(dragonPath,"img","champion","tiles",champId + "_0.jpg")

def getIconItemPath(idItem):
  dragonPath = dragonManip.getDragonPath()
  dragonName = dragonManip.getDragonName()
  return os.path.join(dragonPath, dragonName[11:], "img", "item", idItem + ".png")