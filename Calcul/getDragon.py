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
  
  return  json.loads(itemsJson)

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
  
def getOneChampData():
  pass


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

def getIconChampPath(idChamp):
  dragonPath = dragonManip.getDragonPath()
  return os.path.join(dragonPath,"img","champion","tiles",idChamp + "_0.jpg")

def getIconItemPath(idItem):
  dragonPath = dragonManip.getDragonPath()
  dragonName = dragonManip.getDragonName()
  return os.path.join(dragonPath, dragonName[11:], "img", "item", idItem + ".png")