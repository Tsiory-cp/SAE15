import csv
import matplotlib.pyplot as plt


chemin = "experimentations_5G.csv"
nb_usage={}


with open(chemin, encoding="cp1252", newline="") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=";")
    colonnes=lecteur.fieldnames
#Pour créer un variable qui a pour contenu les noms des colonnes qui commencent par "Usage"
    colonnes_usage=[col for col in colonnes if col.startswith("Usage")]
    #print(colonnes_usage)
    

 # Initialiser les compteurs
 #Si l'initialisation du compteur se trouve dans les boucles suivantes, le compteur reste à 0
    for col in colonnes_usage:
        nb_usage[col] = 0

    # Parcourir les lignes, repérer les 1 et les compter
    for ligne in lecteur:
        for col in colonnes_usage:
            if ligne[col].strip()=="1":
                nb_usage[col]+=1
    
plt.barh(nb_usage.keys(), nb_usage.values())
plt.show()
    
   