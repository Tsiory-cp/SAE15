import csv

# Chemin vers ton fichier
chemin = r"C:\Users\diakhrok\Downloads\experimentations_5G.csv"

techno_compteur = {}

with open(chemin, encoding="cp1252", newline="") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=";")
    colonnes = lecteur.fieldnames

    # Initialiser les compteurs pour chaque techno
    for col in colonnes:
        if col.startswith("Techno"):
            techno_compteur[col] = set()  # Utiliser un set pour éviter les doublons

    # Parcourir les lignes pour remplir les sets
    for ligne in lecteur:
        nom = ligne["Région"]
        for techno in techno_compteur:
            if ligne[techno] == "1":
                techno_compteur[techno].add(nom)

# Affichage du nombre d’expérimentateurs par techno
for techno, noms in techno_compteur.items():
    print(f"{techno} : {len(noms)} regions")
