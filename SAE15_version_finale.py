import csv  #csv est le module pour lire les fichier .csv 
import matplotlib.pyplot as plt  #c'est le module pour les interfaces graphiques 

chemin = "experimentations_5G.csv"  #on affecte à la variable le nom du fichier à analyser pour ne pas écrire à chaque fois 

#Initialisations des dictionnaires
nb_usage = {} 
compte_regions = {}
compte_operateurs = {}


#Pour la partie répartition des usages 5G 
with open(chemin, encoding="cp1252", newline="") as fichier:             #Pour ouvrir le fichier
    lecteur = csv.DictReader(fichier, delimiter=";")             #on affecte à la variable lecteur la fonction de lire le fochoer en tant qu'un dictionnaire
    colonnes = lecteur.fieldnames                 #Variable pour que le code repère automatiquement les colonnes dans le fichier 
    
    colonnes_usage = [col for col in colonnes if col and col.strip().startswith("Usage")]     # Colonnes qui commencent par usage

    for col in colonnes_usage:            #Une boucle qui va balayer les éléments des colonnes et chaque éléments va être stocker dans la variable col 
        nb_usage[col] = 0            #Initialisation de la boucle pour compter 

    # Comptage des "1" et on ajoute 1 au compteur à chaque fois qu'il y a un 1 dans les colonnes 
    for ligne in lecteur:
        for col in colonnes_usage:
            if col in ligne and ligne[col].strip() == "1":  
                nb_usage[col] += 1

#Diagramme
labels = list(nb_usage.keys())        #On affecte à la variable labels la liste qu'on vient de créer qui contient les types d'usages
valeurs = list(nb_usage.values())       #De même pour les nombres de types d'usage 

#plt.figure(figsize=(8, 8))  # diagramme plus grand
plt.pie(valeurs, labels=labels)   #Pour le créer le diagrammes avec les valeurs du dictionnaire  
plt.title("Répartition des usages 5G")  #Le titre pour le graphique 
plt.tight_layout()
plt.show()



#Pour la partie du nombre de signe par régions 
with open(chemin, encoding="cp1252", newline="") as fichier:
    lecteur = csv.DictReader(fichier, delimiter=";")

    for ligne in lecteur:
        region = ligne["Région"].strip()   #On affecte à la variable opérateur les contenues des lignes Experimentateur et .strip pour supprimer les éventuelles espaces 
        
        # Si la région est nouvelle, on l’ajoute
        if region not in compte_regions:
            compte_regions[region] = 0
        
        # On ajoute un site
        compte_regions[region] += 1

# Afficher les résultats
#print("Nombre de sites par région :\n")
for region, nb in compte_regions.items():  #Pour lister les régions 
    print(region, ":", nb)
    
#barh pour des barres en horizontales, .keys() et .valus pour récupérer les noms et les valuers dans le dictionnaire
plt.barh(compte_regions.keys(),compte_regions.values(), color="green")  #
plt.title("Le nombre de sites par Régions")
plt.ylabel("Les régions")  
plt.xlabel("Les nombre des sites")
plt.show()


#Por la partie "Les expérimentateurs les plus présents en France"
with open(chemin, encoding="cp1252", newline="") as f:
    lecteur = csv.DictReader(f, delimiter=";")

    for ligne in lecteur:
        operateur = ligne["Expérimentateur"].strip()  #On affecte à la variable opérateur les contenues des lignes Experimentateur 

        # Pour les opérateur qui ne sont pas dans le dictionnaire, on ajoute
        if operateur not in compte_operateurs:
            compte_operateurs[operateur] = 0
        compte_operateurs[operateur] += 1

# On trie du plus grand au plus petit
top10 = sorted(compte_operateurs.items(), key=lambda x: x[1], reverse=True)[:10]

# On stocke les opérateurs et leurs valeurs dans 2 listes qu'on va initiliser 
noms = []
valeurs = []

for op, nb in top10:
    noms.append(op)
    valeurs.append(nb)

# On affiche une simple liste
print("Les expérimentateurs les plus présents en France :\n")
print("Expérimentateur / Nombre de sites")
print("---------------------------------")

for i in range(len(noms)):   # Afficher une simple liste 
    print(noms[i], ":", valeurs[i])


#  Diagramme 
labels = [op for op, nb in top10]
valeurs = [nb for op, nb in top10]

plt.figure()
plt.barh(labels, valeurs)
plt.xlabel("Nombre de sites")
plt.title("Top 10 des expérimentateurs les plus présents en France")
plt.gca().invert_yaxis()   # le 1er en haut
plt.tight_layout()
plt.show()




