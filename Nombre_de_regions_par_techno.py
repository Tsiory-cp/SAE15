import matplotlib.pyplot as plt #pour la creation du graphique 
import csv 
import matplotlib.pyplot as plt #import matplotlib.pyplot as plt

# Chemin vers ton fichier
chemin = r"C:\Users\diakhrok\Downloads\experimentations_5G.csv"

techno_compteur = {}

#J'ouvre le fichier csv 
with open(chemin, encoding="cp1252", newline="") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=";")
    colonnes = lecteur.fieldnames # je parcours les colonnes 

    # Initialiser les compteurs pour chaque techno
    for col in colonnes:
        if col[:6]=="Techno":
            techno_compteur[col] = set()  # Utiliser un set pour éviter les doublons

    # Parcourir les lignes pour remplir les sets
    for ligne in lecteur:
        nom = ligne["Région"]
        for techno in techno_compteur:
            if ligne[techno] == "1":
                techno_compteur[techno].add(nom)

# Transformer en listes pour le graphique
techno_labels = list(techno_compteur.keys())
nombre_regions = [len(noms) for noms in techno_compteur.values()]

# Création du graphique en courbe
plt.figure(figsize=(10,6))
plt.plot(nombre_regions, techno_labels, marker='o', linestyle='-', color='purple')
plt.title("Nombre de régions par technologie")
plt.xlabel("Technologies")
plt.ylabel("Nombre de régions")
plt.grid()
plt.title("Nombre de régions par technologie")
plt.xlabel("Technologies")
plt.ylabel("Nombre de régions")
plt.grid()
# Rotation des labels parceque les noms sont beaucoup trop longue 
plt.xticks(rotation=35)
plt.savefig("Nombre de regions par technologie.png")
plt.show()

# Affichage du nombre d’expérimentateurs par techno
for techno, noms in techno_compteur.items():
    print(f"{techno} : {len(noms)} regions")