"""
Projekt Bibliothek

Schreibe eine Software für eine Bibliothek.
-   Beim Start sollen ein Medienkatalog und ein
    Kundenregister aus CSV- Dateien ausgelesen werden.
-   Anschließend soll ein Konsolenmenü/ Dialog
    erscheinen, worüber folgende Aufgaben 
    ausgewählt werden können:
    -   Medienverleih   (*1)
    -   Medienrückgabe  (*2)
    -   Mediensuche (nach ID, Autor/Künstler oder 
                     Titel bzw. Teilen davon)
    -   Medien hinzufügen
    -   Neukunden registrieren
    -   Kundensuche (z.B. Rückgabefrist überschritten)
-   Beim Beenden der Software sollen die aktualisierten
    Daten des Medienkatalogs und des Kundenregisters in 
    die CSV- Dateien zurückgeschrieben werden.

ad *1) Beim Verleih sollen der Verleihstatus und das 
       Rückgabedatum entsprechend gesetzt werden.
ad *2) Bei der Rückgabe soll der letzte Nutzer aktualisiert 
       werden.

Überlegungen für einen objektorientierten Ansatz:

Klasse Bibliothek:
-   Attribute: Medienkatalog, Kundenregister
-   Methoden: Die in der Beschreibung aufgeführten.

Klasse Media:
-   Attribute:
    -   ID (ISBN, EAN)
    -   Medientyp (Buch, Zeitschrift, CD, DVD)
    -   Autor/Künstler
    -   Titel
    -   Verleihstatus
    -   Rückgabedatum (wenn verliehen)


Klasse Kunde
-   Attribute:
    -   Kundennummer (Initialen-Quartal-Jahr, z.B. SK-Q4-2024)
    -   Name
    -   Adresse
    -   Liste geliehener Medien  

"""
import csv
from datetime import datetime
import time

# Aktuelles Datum im Format YYYY-MM-DD
current_date = datetime.now().strftime("%Y-%m-%d")
print(current_date)

class Media():
    def __init__(self,id, typ, autor, titel, status, r_datum, letzterNutzer):
        self.id = id
        self.typ = typ
        self.autor = autor
        self.titel = titel
        self.status = status
        self.r_datum = r_datum
        self.letzterNutzer = letzterNutzer
    def __repr__(self):
        return f"{50*"-"}\nMedien ID: {self.id}\nMedien Typ: {self.typ}\nAutor/ Künstler: {self.autor}\nTitel: {self.titel}\nStatus: {self.status}\nRückgabe: {self.r_datum}\nLetzter Nutzer: {self.letzterNutzer}"


class Kunde():
    def __init__(self,name,sex,adresse,knr,leihstatus,geliehen):
        self.knr = knr
        self.name = name
        self.sex = sex
        self.adresse = adresse
        self.leihstatus = leihstatus
        self.geliehen = geliehen
    def __repr__(self):
        return f"{50*"-"}\n{self.sex}\n{self.name}\nAdresse: {self.adresse}\nLeihstatus: {self.leihstatus}\n{self.geliehen.strip()}\n"

class Bibliothek():
    def __init__(self):
        self.modus = ""
        self.pathMedia = "D:/Projekte/Softwareprojekte/Python/Projekt Bibliothek/media.csv"
        self.pathKunde = "D:/Projekte/Softwareprojekte/Python/Projekt Bibliothek/customer.csv"
        self.catMedia = self.loadMediaCSV()
        self.regKunde = self.loadKundeCSV()
        self.dialog()
    def loadMediaCSV(self):
        with open(self.pathMedia) as mediaCSV:
            # return list(csv.DictReader(mediaCSV, delimiter=";"))
            # ID;Typ;Autor;Titel;Status;Rueckgabe;LetzterNutzer
            return [Media(m["ID"],m["Typ"], m["Autor"], m["Titel"], m["Status"],m["Rueckgabe"], m["LetzterNutzer"] ) for m in csv.DictReader(mediaCSV, delimiter=";")]
    def loadKundeCSV(self):
        with open(self.pathKunde, encoding="utf-8") as custCSV:
            # return list(csv.DictReader(custCSV, delimiter=";"))
            # name; sex; address; cID; leihstatus; gelieheneMedien
            return [Kunde(k["name"],k["sex"],k["address"],k["cID"],k["leihstatus"],k["gelieheneMedien"]) for k in csv.DictReader(custCSV, delimiter=";")]
    def showAllMedia(self):
        for m in self.catMedia:
            # print(f"{50*"-"}\nMedien ID: {m.id}\nMedien Typ: {m.typ}\nAutor/ Künstler: {m.autor}\nTitel: {m.titel}\nStatus: {m.status}\nRückgabe: {m.r_datum}\nLetzter Nutzer: {m.letzterNutzer}")
            print(m)
    def showAllCustomers(self):
        for k in self.regKunde:
            print(k)
    def saveMediaToCSV(self):
        pass
    def saveKundeToCSV(self):
        pass
    def searchMedia(self):
        print("Wonach soll gesucht werden?\n1   Medien ID\n2    Autor\n3    Titel\n4    Verspätungen")
        modus = input("Eingabe Suchmodus: ")
        search = input("Suchbegriff: ")
        for m in self.catMedia:
            match modus:
                case "1":
                    if search in m.id:
                        print(m)
                case "2":
                    if search in m.autor:
                        print(m)
                case "3":
                    if search in m.titel:
                        print(m)
                case "4":
                    if m.r_datum != "" and m.r_datum < current_date:
                        print(m)            
    
    def terminate(self):
        self.saveMediaToCSV()
        self.saveKundeToCSV()
    def dialog(self):      
        while self.modus != "x":
            print("""
            Welche Aufgabe soll erledigt werden?
                  
            1   Verleih Medium
            2   Rückgabe Medium
            3   Anzeige aller Medien
            4   Suche Medium
            5   Neues Medium
            6   Anzeige aller Kunden
            7   Suche Kunde
            8   Neuer Kunde
            x   Programm beenden                 
                  """)
            self.modus = input("Eingabe: ")
            match self.modus:
                case "3":
                    self.showAllMedia()
                case "4":
                    self.searchMedia()
                case "6":
                    self.showAllCustomers()
                case "x":
                    self.terminate()



bib = Bibliothek()



