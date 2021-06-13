#PyQt import
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QMainWindow, QPushButton, QHBoxLayout, QWidget, QGroupBox, QGridLayout, QScrollArea
from PyQt5 import QtGui
from PyQt5 import QtCore

#Module Calcul import
import Calcul.buildManip as build
import Calcul.getDragon as getDragon

#autre import
import sys 


#ON ne met que les modules consernant PyQT 
#Servant à afficher des choses UNIQUEMENT 
#Aucune fonction ne doit avoir besoin du packet "Calcul"

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

    #Paramètres
    self.setWindowIcon(QtGui.QIcon("./img/iconTCTool.png"))
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
    self.generalLayout.addWidget(self.statPanel(), 1, 3, 2, 1)

    self.mainWidget.setLayout(self.generalLayout)

#==================FONCTION CREATION ELEMENTS INTERFACE===========================
  
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

  def statPanel(self):
    """ Creation du panneaux des statistiques"""
    gridStat = QGridLayout()
    gridStat.setSpacing(1)
    
    #Creation du contenu
    listStat = ["HP","Mana","Vitesse de deplacement","Armure","Resistance magique" ,"Range","Regen de vie","Regen de mana","Crit chance","AD","AS","AP","LifeSteal"]
    for i in range (1,14,1):
      pixmap = QtGui.QPixmap("./img/icon"+ str(i) +".png")
      statIconLabel = QLabel()
      statIconLabel.setPixmap(pixmap)
      gridStat.addWidget(statIconLabel, i, 0)
      statValeurLabel = QLabel()
      if(i == 11):
        statValeurLabel.setText(listStat[i-1]+ ": " +str(round(self.build["statsTotal"][listStat[i-1]]["Total"],3)))
      elif i == 9 or i == 13:
        statValeurLabel.setText(listStat[i-1]+ ": " +str(round(self.build["statsTotal"][listStat[i-1]] * 100)) + "%")
      else:
        statValeurLabel.setText(listStat[i-1] + ": " + str(round(self.build["statsTotal"][listStat[i-1]])))
      gridStat.addWidget(statValeurLabel, i, 1)
    
    #Emboitage du panneau
    statBox = QGroupBox("Statistiques")
    statBox.setLayout(gridStat)
    return statBox
      
#=====================FONCTION INTERNE ============================================
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

  #----Fonction d'update----
  def updateChampBuildIcon(self):
    champId = build.getChampName(self.build)
    if champId != "":
      iconChampPath = getDragon.getIconChampPath(champId)
      pixmap = QtGui.QPixmap(iconChampPath).scaled(200,200)
      self.champBuildIcon.setPixmap(pixmap)
  
  def updateItemDeleteMenuInterface(self):
    self.generalLayout.itemAtPosition(1,2).widget().deleteLater()
    self.generalLayout.addWidget(self.itemDeleteMenu(),1,2)

  def updateStatPanel(self):
    self.generalLayout.itemAtPosition(1,3).widget().deleteLater()
    self.generalLayout.addWidget(self.statPanel(), 1, 3, 2, 1)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = IU() 
  window.show() 
  sys.exit(app.exec_())
