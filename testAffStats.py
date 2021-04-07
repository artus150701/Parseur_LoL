
#PyQt import
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys 


#Calcul package import
import Calcul.buildManip
import Calcul.dragonManip

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
    self.generalLayout = QVBoxLayout()
  
    self.msg = QLabel("")
    self.generalLayout.addWidget(self.msg)

    self.button = QPushButton("Show stats", self)
    self.generalLayout.addWidget(self.button)
    self.button.clicked.connect(lambda: self.showStats())

    self.mainWindow.setLayout(self.generalLayout)


  def showStats(self):
    if self.msg.text():
      self.msg.setText("")
    else :
      champDataKey = next(iter(build["champion"]))
      
      statString = "Champion : " + build["champion"][champDataKey]["name"] + " | level = " + str(build["champion"]["level"]) + "\n"

      statString += "\nObjets :\n"
      itemSet = build["items"]

      for x in itemSet:
        statString += "->" + itemSet[x]["name"] + "\n"

      statString += "\nStats : \n"
      stats = build["statsTotal"]
      for key, value in stats.items():
        if key == "AS":
          statString += "AS =" +  str(round(stats['AS']['Total'], 3)) + "\n"
        else:
          statString += key + "=" + str(round(value)) + "\n"

      self.msg.setText(statString)



if __name__ == "__main__":
  Calcul.dragonManip.dragonUpdate()
  build = {
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
  Calcul.buildManip.addItem(build, "Spatule dorée")
  Calcul.buildManip.calculTotalStats(build)

  app = QApplication(sys.argv)


  window = Window()

  sys.exit(app.exec_())
