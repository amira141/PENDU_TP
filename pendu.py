from encodings import utf_8
import os


"""***JEU DU PENDU SIMPLE***"""
"""***Cette version du pendu est simplifiée.***"""
"""***Le score commence à 0 et ne prend pas en charge de profil utilisateur***"""

"""module spécifique au jeu """
from random import choice

#DECLARATION DES VARIABLES


liste_pendu = ["poulet", "bonbon", "maman"]
reservoir = []
continue_partie = True


#AFFICHAGE DU MOT PAR LORDINATEUR 

print("Bienvenue sur notre pendu en ligne.")

mot_pendu = choice(liste_pendu)
print("TEST DU MOT",mot_pendu)
print("Voici le mot à deviner:")

for lettres in mot_pendu :
    lettres_etoile = str.maketrans(lettres,"*")
    print(lettres.translate(lettres_etoile))
    

#JEU 

i = 0
i = int(i)

while i<8 :
    
    while continue_partie : 
        lettre_u = input("Devinez une lettre du mot.")
    
        reservoir.append(lettre_u)
        print("Les lettres que vous avez déjà tapé sont:",reservoir)

        i = i + 1 
        print("Il vous reste",(8- i), "essais")

        if i==8 :
            continue_partie = False
    
        for lettre_r in reservoir :
            if lettre_r == lettres in mot_pendu :
                print("Bravo, vous avez gagné!")
                continue_partie = False
            
    
else:
    print("Désolé, vous avez perdu! Bye!") 
    
    



os.system("pause")

