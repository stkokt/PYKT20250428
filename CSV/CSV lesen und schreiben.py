import csv

# Personen-CSV-Datei erstellen
csv_daten = """Name;Alter;Stadt
Anna;28;Berlin
Max;34;Hamburg
Lisa;23;München\n"""

with open('Personen.csv', 'w') as csv_datei:
    csv_datei.write(csv_daten)

# Lesen mit csv.reader
print("Lesen mit csv.reader:")
with open('Personen.csv', 'r') as csv_datei:
    csv_leser = csv.reader(csv_datei, delimiter=";")
    for zeile in csv_leser:
        print(zeile)

# Lesen mit csv.DictReader
print("\nLesen mit csv.DictReader:")
with open('Personen.csv', 'r', newline='') as csv_datei:
    csv_dict_leser = csv.DictReader(csv_datei, delimiter=";")
    for zeile in csv_dict_leser:
        print(zeile)

# Schreiben mit csv.writer
print("\nSchreiben mit csv.writer:")
neue_daten = [
    ["Tim", 45, "Köln"],
    ["Julia", 29, "Frankfurt"]
]

with open('Personen.csv', 'a', newline='') as csv_datei:
    csv_schreiber = csv.writer(csv_datei, delimiter=";")
    gefilterte_daten = [zeile for zeile in neue_daten if zeile]
    csv_schreiber.writerows(gefilterte_daten)

# Schreiben mit csv.DictWriter
print("\nSchreiben mit csv.DictWriter:")
neue_dict_daten = [
    {"Name": "Paul", "Alter": 31, "Stadt": "Stuttgart"},
    {"Name": "Maria", "Alter": 27, "Stadt": "Düsseldorf"}
]

with open('Personen.csv', 'a', newline='') as csv_datei:
    feldnamen = ["Name", "Alter", "Stadt"]
    csv_dict_schreiber = csv.DictWriter(csv_datei, fieldnames=feldnamen, delimiter=";")
    csv_dict_schreiber.writerows(neue_dict_daten)

# Inhalte der aktualisierten CSV-Datei anzeigen
print("\nAktualisierte CSV-Datei:")
with open('Personen.csv', 'r', newline='') as csv_datei:
    print(csv_datei.read())
