from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QHBoxLayout, QWidget, QGroupBox, QGridLayout, QScrollArea
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys 

import interface

import Calcul.dragonManip as dragonManip
import Calcul.buildManip as buildManip
import Calcul.getDragon as getDragon



import functools
import pprint

#Ce module fait le lien entre l'interface et le module de calcule
#Aucune fonction ne doit retourné quoi que ce soit ici
#Elles sont sensé appellée d'autre fonctions de modules en réaction à des entrées d'utilisateur


class TCToolControl: #Theory Crafting Tool Control
  "Controleur reliant l'interface utilisateur aux fonctions de calcules"

  def __init__(self, IU):
        """Controller initializer."""
        self.IU = IU
        # Connect signals and slots
        self.connectSignals()
  
  def connectSignals(self):
    #Connect Main Menu
    
    #NADA
    
    #Connect ChampSelectMenu
    for champButton in self.IU.champButtonList:
      self.connectButton(button=champButton[0], itemId=champButton[1], function=self.champClicked)
    
    #Connect itemSelectMenu
    for itemButton in self.IU.itemButtonList:
      self.connectButton(button=itemButton[0], itemId=itemButton[1], function=self.itemClicked)
    
    #Connect itemDeleteButton
    for itemDeleteButton in self.IU.itemDeleteButtonList:
      self.connectButton(button=itemDeleteButton[0], itemId=itemDeleteButton[1], function=self.itemDeleteClicked)
    
    #Connect champLevelMenu
    


  def itemDeleteClicked():
    pass
  
  def champClicked(self, champId):
    buildManip.addChampion(self.IU.build, champId)
    buildManip.calculTotalStats(self.IU.build)
    
  
  def itemClicked(self, itemId):
    if not(buildManip.addItem(self.build, itemId)):
      print("YO T AS TROP D ITEM LA ")
    buildManip.calculTotalStats(self.build)
    pprint.pprint(self.IU.build)

  """CONNEXION SIGNALES"""
  def connectButton(self, button, itemId, function ):
    button.clicked.connect(functools.partial(function, itemId))






if __name__ == "__main__":
  app = QApplication(sys.argv)
  
  IU = interface.IU()  #Interface Utilisateur
  IU.show()
  
  IU.levelSelector.currentIndex()
  IU.levelSelector.currentText()
  
  TCToolControl(IU=IU)
  
  sys.exit(app.exec_())


