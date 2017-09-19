from encodings import utf_8
import os 

"""***JEU DU PENDU SIMPLE***"""
"""***Cette version du pendu est simplifiée.***"""
"""***Le score commence à 0 et ne prend pas en charge de profil utilisateur***"""

"""module spécifique au jeu"""
from random import choice 

#LES VARIABLES 

"""
liste_pendu_8 : liste des mots de 8 lettres dans laquelle l'ordinateur va en choisir un a faire deviner.

tours : il s'agit du nombre de chances autorisées 

mot_pendu : mot choisi dans la liste par l'ordinateur pour le faire deviner à l'utilisateur

lettres_etoile : il s'agit des lettres du mots à deviner transformées en étoiles

L : il s'agit d'une variable représentant un espace 

lettres : il s'agit des lettres du mot choisi par l'ordinateur 

 """


liste_pendu_8 = ["pas", "bonbon", "mama"]
tours = 8 

#AFFICHAGE D'UN MOT PAR L'ORDINATEUR 

mot_pendu = choice(liste_pendu_8)
print(mot_pendu) 

print("Voici le mot à deviner:")

for lettres in mot_pendu :
        lettres_etoile = str.maketrans(lettres,"*")
        print(lettres.translate(lettres_etoile))


#MOT MODIFIE PAR LES ETOILES
L = ""

lettre_u = input("Veuillez saisir une lettre ")

for lettres in mot_pendu :
    if lettres in lettre_u:
        L = L + lettres
    else:
        L= L + "*"
 
print(L) 

#PARTIE DE PENDUE








os.system("pause")