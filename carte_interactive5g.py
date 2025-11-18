import csv
import folium

# Nom du fichier CSV (dans le même dossier que le notebook)
fichier_csv = "experimentations_5G.csv"

# Noms des colonnes (d'après ce que tu as affiché)
col_lat = "Latitude"
col_lon = "Longitude"
col_region = "Région"
col_exp = "Expérimentateur"
col_bande = "Bande de fréquences"

# Liste pour stocker les points (latitude, longitude, texte du popup)
liste_points = []

with open(fichier_csv, encoding="cp1252", newline="") as f:
    lecteur = csv.DictReader(f, delimiter=";")

    for ligne in lecteur:
        # récupération des coordonnées
        lat_texte = ligne[col_lat].strip()
        lon_texte = ligne[col_lon].strip()

        if lat_texte == "" or lon_texte == "":
            continue  # on saute si coordonnée manquante

        lat_texte = lat_texte.replace(",", ".")
        lon_texte = lon_texte.replace(",", ".")

        try:
            latitude = float(lat_texte)
            longitude = float(lon_texte)
        except ValueError:
            continue  # on saute si ce n'est pas un nombre

        region = ligne[col_region].strip()
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
