
#PyQt import
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QHBoxLayout, QWidget, QGroupBox, QGridLayout, QScrollArea
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys 

import Calcul.dragonManip as dragon
import Calcul.buildManip as build
import Calcul.getDragon as getDragon

import functools

import pprint

class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.title = "LOL_TheoryCrafting_Tool"
    self.width = 1600
    self.height = 900
    self.iconName = "iconTTool.png"
    self.build = build.createBuild()
    self.build = {
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
    build.setLevelChampion(self.build, 18)

    self.setWindowIcon(QtGui.QIcon(self.iconName))
    self.setWindowTitle(self.title)
    self.setFixedSize(self.width, self.height)

    self.mainWindow = QWidget(self)
    self.setCentralWidget(self.mainWindow)
    

    self.UiComponents()

    self.show()
  

  def UiComponents(self):

    gridChampion = QGridLayout()
    gridChampion.setSpacing(1)

    gridItem = QGridLayout()
    gridItem.setSpacing(1)

    gridStat = QGridLayout()
    gridStat.setSpacing(1)
    
    
    championBox = QGroupBox("Champions")
    itemsBox = QGroupBox("items")
    statBox = QGroupBox("Statistiques")
    
    # ================================PARSEUR BOUTON A METTRE ICI=================================================

    championIdList = getDragon.getListChampionId()
    championButtonList = []

    for champId in championIdList:
      iconChampPath = getDragon.getIconChampPath(champId)
      championButtonList.append(QPushButton(""))
      championButtonList[-1].setIcon(QtGui.QIcon(iconChampPath))
      championButtonList[-1].setFixedSize(110,110)
      championButtonList[-1].setIconSize(QtCore.QSize(100,100))
      self.connectButtonChamp(championButtonList[-1], champId)

    itemIdList = getDragon.getLisItemId()
    itemButtonList = []

    for itemId in itemIdList:
      iconItemPath = getDragon.getIconItemPath(itemId)
      itemButtonList.append(QPushButton(""))
      itemButtonList[-1].setIcon(QtGui.QIcon(iconItemPath))
      itemButtonList[-1].setFixedSize(75,75)
      itemButtonList[-1].setIconSize(QtCore.QSize(100,100))
      self.connectButtonItem(itemButtonList[-1], itemId)
      


    # =====================================================================================================
    
    #PARAMETRE BOXES
    nbColonnesChamp = 4
    nbColonnesItems = 6
    compteur = 0

    # -(- numerateur // denominateur) petit trick pour avoir une division entière arrondie au nombre supérieur
    # ça évite d'importer "math.ceil()" + c'est + rapid
    #Comme ça on a le nombre de ligne nécessaire pour mettre tout les boutons

    #définition de la grille de champions
    for i in range( -(- len(championButtonList) // nbColonnesChamp)): 
      for j in range(nbColonnesChamp):
        gridChampion.addWidget(championButtonList[compteur], i, j) #  i lignes | j colonnes
        compteur += 1
        if compteur == len(championButtonList): #On s'arrête une fois la liste de bouton complètement parcouru
          break
    
    #définition de la grille d'items
    compteur = 0
    for i in range( -(- len(itemButtonList)//nbColonnesItems)): 
      for j in range(nbColonnesItems):
        gridItem.addWidget(itemButtonList[compteur], i, j) # j colonnes | i lignes
        compteur += 1
        if compteur == len(itemButtonList): #On s'arrête une fois la liste de bouton complètement parcouru
          break
    
    #définition de la grille des stats
    statLabel =  QLabel("ici on mettra les stas\n avec les icons tout ça tout ça")
    gridStat.addWidget(statLabel)
    

    championBox.setLayout(gridChampion)
    championScroll = QScrollArea()
    championScroll.setWidget(championBox)
    championScroll.setWidgetResizable(True)
    championScroll.setFixedHeight(600)

    itemsBox.setLayout(gridItem)
    itemScroll = QScrollArea()
    itemScroll.setWidget(itemsBox)
    itemScroll.setWidgetResizable(True)
    itemScroll.setFixedHeight(600)

    statBox.setLayout(gridStat)


    finalLayout = QGridLayout()
    finalLayout.addWidget(championScroll, 2, 1)
    finalLayout.addWidget(itemScroll, 2, 2)
    finalLayout.addWidget(statBox, 2, 3 )


    self.mainWindow.setLayout(finalLayout)
  

  #CONTROLEUR
  def champClicked(self, champId):
    build.addChampion(self.build, champId)
    build.calculTotalStats(self.build)
  
  def itemClicked(self, itemId):
    if not(build.addItem(self.build, itemId)):
      print("YO T AS TROP D ITEM LA ")
    build.calculTotalStats(self.build)
    pprint.pprint(self.build)

  def connectButtonChamp(self, button, champId):
    button.clicked.connect(functools.partial(self.champClicked, champId ))

  def connectButtonItem(self, button, itemId):
    button.clicked.connect(functools.partial(self.itemClicked, itemId ))




if __name__ == "__main__":
  app = QApplication(sys.argv)
  dragon.dragonUpdate()
  window = Window()  
  sys.exit(app.exec_())
