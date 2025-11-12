import csv
import matplotlib.pyplot as plt


# Chemin vers ton fichier
chemin = "experimentations_5G.csv"

# Dictionnaire pour compter les régions
compte_regions = {}


with open(chemin, encoding="cp1252", newline="") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=";")

    for ligne in lecteur:
        region = ligne["Région"].strip()   # lit la région
        
        # Si la région est nouvelle → on l’ajoute
        if region not in compte_regions:
            compte_regions[region] = 0
        
        # On ajoute un site
        compte_regions[region] += 1

# Afficher les résultats
print("Nombre de sites par région :\n")
for region, nb in compte_regions.items():
    print(region, ":", nb)
    
#barh pour des barres en horizontales, .keys() et .valus pour récupérer les noms et les valuers dans le dictionnaire
plt.barh(compte_regions.keys(),compte_regions.values()) 
plt.title("Le nombre de sites par Régions")
plt.ylabel("Les régions")
plt.xlabel("Les nombre des sites")
plt.show()
    


