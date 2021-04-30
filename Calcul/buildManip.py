from .getDragon import getOneItemData, getOneChampData
from .subModule.utileProg import doubleIterate, removesuffix
from .subModule.tradStats import tradStatChamp, tradStatItem


def createBuild():
  build = {
      "champion": {
          "level": 1,
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
  return build

#-----------Gestion des items---------------


def removeItem(build, item):
  if item in build["items"]:
    del build["items"][item]
    return True
  else:
    return False


def addItem(build, item):
  if len(build["items"]) < 6:
    data = getOneItemData(item)
    if data:
      build["items"][item] = data
      return True, 0
  else:
    #il y a déjà 6 items dans le build
    return False

#-----Gestion Champion---------------------


def removeChampion(build):
  champ = getChampName(build)
  del build["champion"][champ]


def addChampion(build, champion):
  data = getOneChampData(champion)
  if data:
    build["champion"].update(data)
  else:
    return False
  return True


def setLevelChampion(build, level):
  build["champion"]["level"] = level


def getChampName(build):
  for key in build["champion"].keys():
    if key != "level":
      return key
  return ""

#-----Gestion Stats--------------------


def statFormula(base, growth, level):
  return base + growth * (level - 1) * (0.7025 + 0.0175 * (level - 1))


def calculTotalStats(build):
  champDataKey = getChampName(build)
  champLevel = build["champion"]["level"]
  itemSet = build["items"]
  statsTotal = build["statsTotal"]
  statsChamp = build["champion"][champDataKey]["stats"]

  #Calcules stats + lvl
  for stat, next_stat in doubleIterate(statsChamp.items()):

    if stat[0] == "attackspeedperlevel" or not(stat[0].endswith("level")):

      if stat[0] == "attackspeed":
        break

      elif stat[0] == "movespeed" or stat[0] == "attackrange":
        statsTotal[tradStatChamp(stat[0])] = stat[1]

      elif stat[0] == "attackspeedperlevel":
        asBonusPourcent = stat[1] * (champLevel - 1) * \
            (0.7025 + 0.0175 * (champLevel - 1))
        statsTotal[tradStatChamp(next_stat[0])]["Bonus"] += asBonusPourcent/100
        statsTotal[tradStatChamp(next_stat[0])]["Ratio"] = next_stat[1]

      else:
        statsTotal[tradStatChamp(stat[0])] = statFormula(
            stat[1], next_stat[1], champLevel)

  #Calcules stats + items
  for selectItem in itemSet:
    itemStats = itemSet[selectItem]["stats"]
    for selectStat in itemStats:
      if selectStat.startswith('Flat'):
        statsTotal[tradStatItem(removesuffix(
            selectStat.lstrip("Flat"), "Mod"))] += itemStats[selectStat]
      elif "AttackSpeed" in selectStat:
        statsTotal["AS"]["Bonus"] += itemStats[selectStat]
      else:
        statsTotal[tradStatItem(removesuffix(selectStat.lstrip(
            "Percent"), "Mod"))] *= 1 + itemStats[selectStat]

  #Calcul de L'attaque speed total capé à 2.5
  statsTotal["AS"]["Total"] = (
      statsTotal["AS"]["Ratio"] * (1 + statsTotal["AS"]["Bonus"])) % 2.5
