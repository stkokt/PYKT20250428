# Lese diese Dateien ein
# - Erwerbstaetige1
# - Konsumentwicklung
# - Lohnentwicklung

# Bilde diese Ratios:
# Anteil der Land-, Forst- und Fischereiarbeiter sowie der Dienstleister an den Gesamtbeschäftigten.
# Anteil der Wohn- sowie der Lebenserhaltungskosten (Nahrung/Genuss) am Gesamtkonsum.
# Verhältnis von Netto- zu Bruttolöhnen. 
# 
# Recherchiere, wie du diese Ratios in eine CSV- Datei zurückschreiben kannst. 

import csv
# Einlesen einer CSV-Datei mit csv.DictReader
with open('Erwerbstaetige1.csv', mode='r', newline='') as file:
    csv_dict_reader = csv.DictReader(file, delimiter=";")
    dataErwerb = list(csv_dict_reader)

#print(dataErwerb)

jahre = [ds['Jahr'] for ds in dataErwerb]
# print(jahre)

ratioLFF = [round(float(ds['LandForstFisch'])/float(ds['Insgesamt']),5) for ds in dataErwerb]
#print(ratioLFF)

ratioDL = [round(float(ds['DienstAll'])/float(ds['Insgesamt']),5) for ds in dataErwerb]
#print(ratioDL)

ratios = list(zip(jahre, ratioLFF, ratioDL))
#print(ratios)

ratiosDict = list({"Jahr": ds[0],"ratioLFF": ds[1],"ratioDL": ds[2]} for ds in ratios)

print(ratiosDict)
# Schreiben über DictWriter

with open("output_Dict.csv", mode='w', newline='') as file:
        csv_dict_writer = csv.DictWriter(file, fieldnames=ratiosDict[0].keys(), delimiter=";")
        csv_dict_writer.writeheader()
        for row in ratiosDict:
            csv_dict_writer.writerow(row)



