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
mot_pendu : mot choisi dans la liste par l'ordinateur pour le faire deviner à l'utilisateur
lettres_etoile : il s'agit des lettres du mots à deviner transformées en étoiles 
deviner_lettre : il s'agit de la lettre choisie par l'utilisateur """


score = 0
score = int(score)

continuer_partie = True 

print(" Bienvenue sur le jeu du pendu :) ")

###LE JEU 

#-Choix du mot par l'ordinateur 

while continuer_partie: 

    liste_pendu_8 = ["poulet", "bonbon", "haricot", "patate"] 
    mot_pendu = choice(liste_pendu_8)

    
    print("Voici le mot à deviner:")
    
    for lettres in mot_pendu :
        lettres_etoile = str.maketrans(lettres,"*")
        print(lettres.translate(lettres_etoile))


#-L'utilisateur devine

    i = 1 
    while i<9 :
        deviner_lettre = input("Veuillez saisir une lettre")
        i += 1

        if len(deviner_lettre) >= 2:
            print("Il n'est pas demandé d'écrire un mot.")
            i = 9-i

        


      



#FIN DE LA PARTIE 


os.system("pause")