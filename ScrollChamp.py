
#PyQt import
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QHBoxLayout, QWidget, QGroupBox, QGridLayout, QScrollArea
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys 

import Calcul.dragonManip as dragon

class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.title = "LOL_TheoryCrafting_Tool"
    self.width = 1280
    self.height = 720
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
    gridStat.setSpacing(10)
    
    

    championBox= QGroupBox("Champions")
    itemsBox = QGroupBox("items")
    statBox = QGroupBox("Statistiques")
    
    # ================================PARSEUR BOUTON A METTRE ICI=================================================

    nbButton = 155
    nbColonnes = 4
    compteur = 0
    championList = []
    itemList = []
    #Création d'une série de bouton stocké dans une liste
    for i in range(nbButton):
      championList.append(QPushButton(f"Champion {i}"))
      itemList.append(QPushButton(f"Items {i}"))

    # =================================================================================
    # -(- numerateur // denominateur) petit trick pour avoir une division entière arrondie au nombre supérieur
    # ça évite d'importer "math.ceil()" + c'est + rapid
    #Comme ça on a le nombre de ligne nécessaire pour mettre tout les boutons

    #définition de la grille de champions
    for i in range( -(-nbButton//nbColonnes)): 
      for j in range(nbColonnes):
        gridChampion.addWidget(championList[compteur], i, j) # j colonnes | i lignes
        compteur += 1
        if compteur == nbButton: #On s'arrête une fois la liste de bouton complètement parcouru
          break
    
    #définition de la grille d'items
    compteur = 0
    for i in range( -(-nbButton//nbColonnes)): 
      for j in range(nbColonnes):
        gridItem.addWidget(itemList[compteur], i, j) # j colonnes | i lignes
        compteur += 1
        if compteur == nbButton: #On s'arrête une fois la liste de bouton complètement parcouru
          break
    
    #définition de la grille des stats
    statLabel =  QLabel("ici on mettra les stas\n avec les icons tout ça tout ça")
    gridStat.addWidget(statLabel)
    
    statBox.setLayout(gridStat)


    championBox.setLayout(gridChampion)
    championScroll = QScrollArea()
    championScroll.setWidget(championBox)
    championScroll.setWidgetResizable(True)
    championScroll.setFixedHeight(400)

    itemsBox.setLayout(gridItem)
    itemScroll = QScrollArea()
    itemScroll.setWidget(itemsBox)
    itemScroll.setWidgetResizable(True)
    itemScroll.setFixedHeight(400)


    finalLayout = QHBoxLayout()
    finalLayout.addWidget(championScroll)
    finalLayout.addWidget(itemScroll)
    finalLayout.addWidget(statBox)


    self.mainWindow.setLayout(finalLayout)



if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()  
  sys.exit(app.exec_())
