
#PyQt import
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QHBoxLayout, QWidget, QGroupBox, QGridLayout, QScrollArea
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys 

import Calcul.dragonManip as dragon
import Calcul.buildManip as build
import Calcul.getDragon as getDragon



class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.title = "LOL_TheoryCrafting_Tool"
    self.width = 1600
    self.height = 900
    self.iconName = "iconTTool.png"

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


    itemIdList = getDragon.getLisItemId()
    itemButtonList = []

    for itemId in itemIdList:
      iconItemPath = getDragon.getIconItemPath(itemId)
      itemButtonList.append(QPushButton(""))
      itemButtonList[-1].setIcon(QtGui.QIcon(iconItemPath))
      itemButtonList[-1].setFixedSize(75,75)
      itemButtonList[-1].setIconSize(QtCore.QSize(100,100))


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



  
    finalLayout = QHBoxLayout()
    finalLayout.addWidget(championScroll)
    finalLayout.addWidget(itemScroll)
    finalLayout.addWidget(statBox)


    self.mainWindow.setLayout(finalLayout)



if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()  
  sys.exit(app.exec_())
