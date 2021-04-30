#PyQt import
from pprint import pprint
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QMainWindow, QPushButton, QHBoxLayout, QWidget, QGroupBox, QGridLayout, QScrollArea
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys 

import Calcul.dragonManip as dragon
import Calcul.buildManip as build
import Calcul.getDragon as getDragon


class IU(QMainWindow):
  """Interface du TheoryCrafting Tool"""
  
  def __init__(self):
    super().__init__()
    """Quelques paramètres pour la fenêtre principale"""
    #Attributs
    self.title = "LOL_TheoryCrafting_Tool"
    self.width = 1600
    self.height = 900
    self.build = build.createBuild()

    #TEMPORAIRE CEST DE LA TRICHE OULALALALLAL
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
    build.addItem(self.build, "1037")
    build.addItem(self.build, "1001")
    build.addItem(self.build, "6333")
    build.addItem(self.build, "1058")
    build.addItem(self.build, "3004")
    build.addItem(self.build, "3036")
    pprint(self.build)
    #FIN DE LA TRICHE OULOULUOULUOULUO
    

    #Paramètres
    self.setWindowIcon(QtGui.QIcon("iconTCTool.png"))
    self.setWindowTitle(self.title)
    self.setFixedSize(self.width, self.height)
    #Met en place le principale widget et le layout générale
    self.mainWidget = QWidget(self)
    self.setCentralWidget(self.mainWidget)
    self.generalLayout = QGridLayout()
    #Créations des composants d'interface 
    self.mainMenu()
    self.generalLayout.addWidget(self.champSelectMenu(), 2, 1)
    self.generalLayout.addWidget(self.itemSelectMenu(), 2, 2)
    self.generalLayout.addWidget(self.itemDeleteMenu(), 1, 2)
    self.generalLayout.addWidget(self.champLevelMenu(), 1, 1)

    self.mainWidget.setLayout(self.generalLayout)
    #self.show()
  

#============================FONCTION CREATION BIG WIDGET=========================================
  def mainMenu(self):
    """Creation de la barre des tâches"""
    self.statusBar()
    self.mainMenu = self.menuBar()
    
    """Creation des sous-menu"""
    fichierMenu = self.mainMenu.addMenu('&Fichier')
    editerMenu = self.mainMenu.addMenu('&Editer')
    affichageMenu = self.mainMenu.addMenu('&Affichage')

    """ Creation des Actions"""
    # Action fichier
    # Action Editer
    exportBuild = QtWidgets.QAction("Exporter le build", self)
    # Action Affichage
    blackThemeAction = QtWidgets.QAction("Theme sombre", self)
    whiteThemeAction = QtWidgets.QAction("Theme clair", self)

    """Association des Actions avec le menu"""
    # fichier
    # editer
    editerMenu.addAction(exportBuild)
    # affichage
    affichageMenu.addAction(blackThemeAction)
    affichageMenu.addAction(whiteThemeAction)

  def champSelectMenu(self, nbColonnes=4):
    """Creation du menu de selection de champion"""
    #Création de la Liste des buttons de champions
    champIdList = getDragon.getListChampionId()

    self.champButtonList = [] #Liste de tuples composé de button et de l'id de leur champion correspondant
    for champId in champIdList:
      self.champButtonList.append((QPushButton(""),champId))
      self.setChampButton(self.champButtonList[-1][0], champId)
    
    #Création de la grille de champion
    champGrid = QGridLayout()
    champGrid.setSpacing(1)
    
    compteur = 0
    for i in range( -(- len(self.champButtonList) // nbColonnes)): #divisions arrondie supérieur
      for j in range(nbColonnes):
        if compteur == len(self.champButtonList): #On s'arrête une fois la liste de bouton complètement parcouru
          break
        champGrid.addWidget(self.champButtonList[compteur][0], i, j) #  i lignes | j colonnes
        compteur += 1
        
    
    #Création du menu
    champBox = QGroupBox("Champions")
    champBox.setLayout(champGrid)
    
    champWidget = QScrollArea()
    champWidget.setWidget(champBox)
    champWidget.setWidgetResizable(True)
    champWidget.setFixedHeight(600)

    return champWidget

  def itemSelectMenu(self, nbColonnes=6):
    """Creation du menu de selection de item"""
    #Création de la Liste des buttons de items
    itemIdList = getDragon.getLisItemId()
    self.itemButtonList = [] #Liste de tuples composé de button et de l'id de leur item correspondant
    for itemId in itemIdList:
      self.itemButtonList.append((QPushButton(""),itemId))
      self.setItemButton(self.itemButtonList[-1][0], itemId)
    
    #Création de la grille de item
    itemGrid = QGridLayout()
    itemGrid.setSpacing(1)
    
    compteur = 0
    for i in range( -(- len(self.itemButtonList) // nbColonnes)): #divisions arrondie supérieur
      for j in range(nbColonnes):
        if compteur == len(self.itemButtonList): #On s'arrête une fois la liste de bouton complètement parcouru
          break
        itemGrid.addWidget(self.itemButtonList[compteur][0], i, j) #  i lignes | j colonnes
        compteur += 1
        
    
    #Création du menu
    itemBox = QGroupBox("Items")
    itemBox.setLayout(itemGrid)
    
    itemWidget = QScrollArea()
    itemWidget.setWidget(itemBox)
    itemWidget.setWidgetResizable(True)
    itemWidget.setFixedHeight(600)

    return itemWidget
  
  def itemDeleteMenu(self):
    """Creation du menu de suppresion d'items"""
    #Creation liste des buttons d'effacement d'items
    self.itemDeleteButtonList = []
    for itemId in self.build["items"].keys():
      self.itemDeleteButtonList.append((QPushButton(""), itemId))
      self.setItemButton(self.itemDeleteButtonList[-1][0], itemId)
    
    #Creation de la grille
    itemDeleteGrid = QGridLayout()
    itemDeleteGrid.setSpacing(1)
    compteur = 0

    for i in range(2): #ligne
      for j in range(3): #colonnes
        if compteur == len(self.itemDeleteButtonList): #On s'arrête une fois la liste de bouton complètement parcouru
          break
        itemDeleteGrid.addWidget(self.itemDeleteButtonList[compteur][0], i, j) #  i lignes | j colonnes
        compteur += 1
    
    #Création du menu
    itemDeleteBox = QGroupBox("Build")
    itemDeleteBox.setLayout(itemDeleteGrid)    
    
    return itemDeleteBox
  
  def champLevelMenu(self):
    """Creation du menu de selection de level"""
    #Création de la combo Box
    self.levelSelector = QComboBox()
    for i in range(1,19):
      self.levelSelector.addItem(str(i))
    
    levelText = QLabel("Niveaux :")

    #Icon du champion
    self.champBuildIcon = QLabel()
    self.updateChampBuildIcon()

    #Création du menu
    champLevelLayout = QHBoxLayout()
    champLevelLayout.addWidget(self.champBuildIcon)
    champLevelLayout.addWidget(levelText)
    champLevelLayout.addWidget(self.levelSelector)
    
    champLevelBox = QGroupBox("Statut")
    champLevelBox.setLayout(champLevelLayout)
    
    return champLevelBox

#=====================FONCTION AUXILIERE ============================================
  def setChampButton(self, champButton, champId):
    iconChampPath = getDragon.getIconChampPath(champId)
    champButton.setIcon(QtGui.QIcon(iconChampPath))
    champButton.setFixedSize(110,110)
    champButton.setIconSize(QtCore.QSize(100,100))

  def setItemButton(self, itemButton, itemId):
    iconItemPath = getDragon.getIconItemPath(itemId)
    itemButton.setIcon(QtGui.QIcon(iconItemPath))
    itemButton.setFixedSize(75,75)
    itemButton.setIconSize(QtCore.QSize(100,100))

  def updateChampBuildIcon(self):
    champId = build.getChampName(self.build)
    if champId != "":
      iconChampPath = getDragon.getIconChampPath(champId)
      pixmap = QtGui.QPixmap(iconChampPath).scaled(200,200)
      self.champBuildIcon.setPixmap(pixmap)
      


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = IU() 
  window.show() 
  sys.exit(app.exec_())
