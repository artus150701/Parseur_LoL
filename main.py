#PyQt import
from PyQt5.QtWidgets import QApplication

#TCTool packets import
import interface
import Calcul.dragonManip as dragonManip
import Calcul.buildManip as buildManip

#autre import
import sys 
import functools

#Ce module fait le lien entre l'interface et le module de calcule
#Aucune fonction ne doit retourné quoi que ce soit ici
#Elles sont sensé appellée d'autre fonctions de modules en réaction à des entrées d'utilisateur


class TCTool(interface.IU): #Theory Crafting Tool Control
  "Controleur reliant l'interface utilisateur aux fonctions de calcules"

  def __init__(self):
    super().__init__()
    
    # Connect signals and slots
    self.connectSignals()


  """<----------- CONNEXION SIGNALES ----------->"""
  def connectSignals(self):
    #Connect Main Menu
    
    #NADA
    
    #Connect ChampSelectMenu
    for champButton in self.champButtonList:
      self.connectButton(button=champButton[0], buttonId=champButton[1], function=self.champClicked)
    
    #Connect itemSelectMenu
    for itemButton in self.itemButtonList:
      self.connectButton(button=itemButton[0], buttonId=itemButton[1], function=self.itemClicked)
    
    #Connect itemDeleteButton
    for itemDeleteButton in self.itemDeleteButtonList:
      self.connectButton(button=itemDeleteButton[0], buttonId=itemDeleteButton[1], function=self.itemDeleteClicked)
    
    #Connect champLevelMenu
    self.levelSelector.currentIndexChanged.connect(functools.partial(self.levelClicked))
  
  
  #============ CONNEXION SECONDAIRE =================
  def updateItemDeleteMenu(self):
    self.updateItemDeleteMenuInterface()
    for itemDeleteButton in self.itemDeleteButtonList:
      self.connectButton(button=itemDeleteButton[0], buttonId=itemDeleteButton[1], function=self.itemDeleteClicked)
    
  def connectButton(self, button, buttonId, function ):
    button.clicked.connect(functools.partial(function, buttonId))


  """<----------- CLICKED ----------->"""
  def itemDeleteClicked(self, itemId):
    buildManip.removeItem(self.build, itemId)
    #Update
    self.updateItemDeleteMenu()
    buildManip.calculTotalStats(self.build)
    self.updateStatPanel()
    
  
  def champClicked(self, champId):
    buildManip.removeChampion(self.build)
    buildManip.addChampion(self.build, champId)
    #Update
    self.updateChampBuildIcon()
    buildManip.calculTotalStats(self.build)
    self.updateStatPanel()

  
  def itemClicked(self, itemId):
    buildManip.addItem(self.build, itemId)
    #Update
    self.updateItemDeleteMenu()
    buildManip.calculTotalStats(self.build)
    self.updateStatPanel()


  def levelClicked(self):
    buildManip.setLevelChampion(self.build, int(self.levelSelector.currentText()))
    buildManip.calculTotalStats(self.build)
    self.updateStatPanel()





if __name__ == "__main__":
  dragonManip.dragonUpdate()
  app = QApplication(sys.argv)
  
  TCTool = TCTool()
  TCTool.show()
  sys.exit(app.exec_())


