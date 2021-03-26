import json
import os
from . import dragonManip


def dataItem(itemTarget):
  dragonPath = dragonManip.getDragonPath()
  dragonName = dragonManip.getDragonName()
  pathItem = os.path.join(dragonPath, dragonName[11:], "data", "fr_FR", "item.json")
    
  with open(pathItem, "r") as itemsFile:
    itemsData = itemsFile.read()
  dragon = json.loads(itemsData)

  for x in dragon["data"]:
    if(itemTarget == dragon["data"][x]["name"]):
      return dragon["data"][x]

  return False

