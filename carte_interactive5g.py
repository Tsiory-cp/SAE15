import csv
import folium

# Nom du fichier CSV (dans le même dossier courant)
fichier_csv = "experimentations_5G.csv"

# Le programme va chercher dans le fichier CSV les colonnes 
col_lat = "Latitude"
col_lon = "Longitude"
col_region = "Région"
col_exp = "Expérimentateur"
col_bande = "Bande de fréquences"

# Liste pour stocker les points (latitude, longitude, texte du popup)
liste_points = []

with open(fichier_csv, encoding="cp1252", newline="") as f: 
    lecteur = csv.DictReader(f, delimiter=";")  #lis chaque ligne comme un dictionnaire avec les colonnes comme clés

    for ligne in lecteur:
        # récupération la latitude et la longitude
        lat_texte = ligne[col_lat].strip()
        lon_texte = ligne[col_lon].strip()

        if lat_texte == "" or lon_texte == "":
            continue  # on saute si coordonnée manquante

        lat_texte = lat_texte.replace(",", ".") #vu c'est avec python les virgure dans les chiffre son representer sous forme de point donc on remplace les , par des .
        lon_texte = lon_texte.replace(",", ".")

        try:
            latitude = float(lat_texte)
            longitude = float(lon_texte)  #on convertie ca en float 
        except ValueError:
            continue  # on saute si ce n'est pas un nombre

        region = ligne[col_region].strip()  #on recupere les autre données
        exp = ligne[col_exp].strip()
        bande = ligne[col_bande].strip()

        # petit texte qui s'affiche quand on clique sur le point
        popup = (
            f"<b>Région :</b> {region}<br>"
            f"<b>Expérimentateur :</b> {exp}<br>"
            f"<b>Bande de fréquences :</b> {bande}"
        )

        liste_points.append((latitude, longitude, popup))

print("Nombre de sites pris en compte :", len(liste_points))

if len(liste_points) == 0:
    print("Aucun point trouvé, vérifier les colonnes latitude/longitude.")
else:
    # calcul d'un centre approximatif de la carte
    lat_moy = sum(p[0] for p in liste_points) / len(liste_points)
    lon_moy = sum(p[1] for p in liste_points) / len(liste_points)

    # création de la carte
    carte = folium.Map(location=[lat_moy, lon_moy], zoom_start=6)

    # ajout d'un marqueur pour chaque site
    for (lat, lon, texte_popup) in liste_points:
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(texte_popup, max_width=250)
        ).add_to(carte)

    # affichage dans le notebook
    carte
    
carte.save("carte_exps_5G.html")
print("Fichier généré : carte_exps_5G.html")

