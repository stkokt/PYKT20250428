# CSV = comma seperated values

import csv

csv_daten = """Name;Alter;Stadt
Anna;28;Berlin
Max;34;Hamburg
Lisa;23;München
"""

# with open("personen.csv",'w') as csv_datei:
#     csv_datei.write(csv_daten)

with open('personen.csv', 'r') as csv_datei:
    csv_leser = csv.reader(csv_datei)
    next(csv_leser)
    for zeile in csv_leser:
        print(zeile)

neue_daten = [
    ["Tim", 45, "Köln"],
    ["Julia", 29, "Frankfurt"]
]

# with open('personen.csv', 'a', newline='') as csv_datei:
#     csv_schreiber = csv.writer(csv_datei)
#     csv_schreiber.writerows(neue_daten)

# DictReader/Writer

with open("personen.csv", "r") as csv_datei:
    csv_dict_reader = csv.DictReader(csv_datei, delimiter=";")
    for zeile in csv_dict_reader:
        print(zeile)

neue_dict_daten = [
    {"Name": "Paul", "Alter": 31, "Stadt": "Stuttgart", "Straße":"Haupstraße"},
    {"Name": "Maria", "Alter": 27, "Stadt": "Düsseldorf", "Straße":"Haupstraße"}
]

with open('personen.csv', 'a', newline='') as csv_datei:
    feldnamen = ["Name", "Alter", "Stadt", "Straße"]
    csv_dict_schreiber = csv.DictWriter(csv_datei, fieldnames=feldnamen, delimiter=";")
    csv_dict_schreiber.writerows(neue_dict_daten)

with open("personen.csv", "r") as csv_datei:
    csv_dict_reader = csv.DictReader(csv_datei, delimiter=";")
    for zeile in csv_dict_reader:
        print(zeile)

