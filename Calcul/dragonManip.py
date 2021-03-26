#==============================IMPORTATION DES BIBLIOTHEQUES==============================
#Téléchargement et lecture de fichier en ligne
import urllib.request
import requests
import json
#Manipulation et lecture de fichiers / dossiers / chemin d'accès
import os
import shutil
import tarfile


#==============================FONCTIONS==============================
#--------RECUPERATION D'INFORMATION-------
def getDragonName():
  for x in os.listdir(os.getcwd()):
    if("dragontail" == x[0:10]):
        return x
  return ""

def getDragonPath():
  return os.path.join(os.getcwd(), getDragonName())

def getLastPatchDragonName():
  with urllib.request.urlopen("https://ddragon.leagueoflegends.com/realms/euw.json") as response:
      source = response.read()
      data = json.loads(source)
  newestDragonEUW = "dragontail-" + data['v']

  return newestDragonEUW

def checkForUpdate():
  localDragon = getDragonName()
  with urllib.request.urlopen("https://ddragon.leagueoflegends.com/realms/euw.json") as response:
      source = response.read()
      data = json.loads(source)
  newestDragonEUW = "dragontail-" + data['v']

  if(localDragon == newestDragonEUW):
    return False
  else:
    return True

#--------MODIFICATION DU DATA DRAGON-----------------

def removeDragon():
  shutil.rmtree(getDragonPath())


#Telecharge le nom du dernier patch sortie sur le serveur EUW et le compare avec la version du dragontail local
#Si une mise à jour est nécessaire alors on télécharge le nouveau patch et on le remplace par l'ancien
def dragonUpdate():
  if checkForUpdate():
    print("Début de la mise à jour")
    
    removeDragon()
    
    newestDragonEUW = getLastPatchDragonName()
    url = 'https://ddragon.leagueoflegends.com/cdn/' + newestDragonEUW + ".tgz"
    pathNewDragonTGZ = os.path.join(os.getcwd(), newestDragonEUW, ".tgz")

    print("Debut du téléchargement...")
    with open(pathNewDragonTGZ, 'wb') as f:
      with requests.get(url, allow_redirects=True, stream=True) as resp:
	      for chunk in resp.iter_content(chunk_size=512):
		      if chunk:
			      f.write(chunk)
    print("Fin du téléchargement...")

    print("Extraction en cours...")
    tarf = tarfile.open(pathNewDragonTGZ, "r")
    tarf.extractall(os.path.join(os.getcwd(), newestDragonEUW)) 
    tarf.close()
    print("Extraction terminée")

    #On supprime le .tgz et l'ancien dragontail local si il existe
    os.remove(pathNewDragonTGZ)
    print("Fin de la mise à jour")
  else:
    print("Le Data Dragon est à jour ")
    



