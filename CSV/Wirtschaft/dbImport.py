import sqlite3
import csv

# Einlesen einer CSV-Datei mit csv.DictReader
with open('Erwerbstaetige1.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_dict_reader = csv.DictReader(file, delimiter=";")
    dataErwerb = list(csv_dict_reader)

# Verbindung zur SQLite-Datenbank herstellen (oder erstellen, falls sie nicht existiert)
conn = sqlite3.connect('Wirtschaftszahlen.db')
cursor = conn.cursor()

# Tabellen erstellen
def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wirtschaftsleistung (
        "ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "Jahr" INTEGER NOT NULL,
        "Insgesamt" REAL NOT NULL,
        "LandForstFisch" REAL NOT NULL,
        "ProdAll" REAL NOT NULL,
        "ProdBau" REAL NOT NULL,
        "DienstAll" REAL NOT NULL,
        "HandelVerkehrGast" REAL NOT NULL,
        "InformFinanzVermietUnternehmdienst" REAL NOT NULL,
        "OeffentSonstDienst" REAL NOT NULL
    )
    ''')
    conn.commit()

# Daten einfügen
def insert_data():
    # Daten in die Tabelle Wirtschaftsleistung einfügen
    data_to_insert = [
        (row['Jahr'], 
         row['Insgesamt'], 
         row['LandForstFisch'], 
         row['ProdAll'], 
         row['ProdBau'],
         row['DienstAll'], 
         row['HandelVerkehrGast'], 
         row['InformFinanzVermietUnternehmdienst'], 
         row['OeffentSonstDienst'])
        for row in dataErwerb
    ]

    cursor.executemany('''
    INSERT INTO Wirtschaftsleistung (Jahr, Insgesamt, LandForstFisch, ProdAll, ProdBau, DienstAll, HandelVerkehrGast, InformFinanzVermietUnternehmdienst, OeffentSonstDienst)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_to_insert)

    conn.commit()

# Daten abfragen
def select_data():
    cursor.execute('SELECT * FROM Wirtschaftsleistung')
    wirtschaftsleistung = cursor.fetchall()
    print("Wirtschaftsleistung:")
    for row in wirtschaftsleistung:
        print(row)

# Daten aktualisieren
def update_data():
    cursor.execute('''
    UPDATE Wirtschaftsleistung
    SET Insgesamt = 3700.7
    WHERE Jahr = 2021
    ''')
    conn.commit()

# Hauptprogramm
if __name__ == "__main__":
    try:
        create_tables()
        insert_data()
        print("Daten nach dem Einfügen:")
        select_data()
        update_data()
        print("\nDaten nach dem Aktualisieren:")
        select_data()
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        # Verbindung schließen
        conn.close()
