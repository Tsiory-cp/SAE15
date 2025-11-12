import csv

chemin = "C:\\Users\\trabeyac\\Downloads\\experimentations_5G.csv"

op_par_region = {}  

with open(chemin, encoding="cp1252", newline="") as f:
    lecteur = csv.DictReader(f, delimiter=";")

    for ligne in lecteur:
        region = ligne["Région"].strip()               
        operateur = ligne["Expérimentateur"].strip()

        if region not in op_par_region:
            op_par_region[region] = set()  

        op_par_region[region].add(operateur)

for region, experimentateurs in op_par_region.items():
    print(region,":", list(experimentateurs))
