#-------------------FONCTION_TRADUCTION_NOM_STATISTIQUES-----------------------

#Pour traduire le nom des stats en nom plus lisible et commun
def tradStatItem(nom):
  if(nom == 'HPPool'):
    return 'HP'
  if(nom == 'HPRegen'):
    return 'Regen de vie'
  if(nom == 'MPPool'):
    return 'Mana'
  if(nom == 'MovementSpeed'):
    return 'Vitesse de deplacement'
  if(nom == 'Armor'):
    return 'Armure'
  if(nom == 'SpellBlock'):
    return 'Resistance magique'
  if(nom == 'CritChance'):
    return 'Crit chance'
  if(nom == 'PhysicalDamage'):
    return 'AD'
  if(nom == 'AttackSpeed'):
    return "AS"
  if nom == "MagicDamage":
    return "AP"
  if nom == "LifeSteal":
    return "LifeSteal"
  return nom


def tradStatChamp(nom):
  if nom == 'attackrange':
    return "Range"
  if(nom == 'hpregen'):
    return 'Regen de vie'
  if(nom == 'mpregen'):
    return 'Regen de mana'
  if nom == 'hp':
    return 'HP'
  if nom == 'mp':
    return 'Mana'
  if nom == 'movespeed':
    return 'Vitesse de deplacement'
  if nom == 'armor':
    return 'Armure'
  if nom == 'spellblock':
    return 'Resistance magique'
  if nom == 'crit':
    return 'Crit chance'
  if nom == 'attackdamage':
    return 'AD'
  if nom == 'attackspeed':
    return 'AS'
