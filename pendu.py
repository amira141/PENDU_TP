from encodings import utf_8
import os 

"""***JEU DU PENDU SIMPLE***"""
"""***Cette version du pendu est simplifiée.***"""
"""***Le score commence à 0 et ne prend pas en charge de profil utilisateur***"""

#Modules à importer spécifiques au jeu
from random import choice #Permet de choisir un mot au hasard STR dans une LISTE 

#DEBUT DE PARTIE : DECLARER LES VARIABLES 

"""score : le score de l'utilisateur 
liste_pendu_8 : liste des mots de 8 lettres dans laquelle l'ordinateur va en choisir un a faire deviner.
mot_pendu : mot choisi dans la liste par l'ordinateur pour le faire deviner à l'utilisateur"""


score = 0
score = int(score)

continuer_partie = True 

print(" Bienvenue sur le jeu du pendu :) ")

###LE JEU 

#-Choix du mot par l'ordinateur 

liste_pendu_8 = ["poulet", "bonbon", "haricot", "patate"] #c
mot_pendu = choice(liste_pendu)


#-L'utilisateur devine




#FIN DE LA PARTIE 





os.system("pause")