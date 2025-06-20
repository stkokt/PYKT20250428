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
from datetime import datetime, timedelta

# Datum im Format YYYY-MM-DD
def make_date(period_days = 0):
    return (datetime.now() + timedelta(days = period_days)).strftime("%Y-%m-%d")
# Kunden ID z.B. AS-Q4-2000
def make_cID(name:str):
    init = name.split(" ")[0][0] + name.split(" ")[-1][0]
    date = make_date().split("-")
    match int(date[1]):
        case 1|2|3:
            init += "-Q1-" + date[0]
        case 4|5|6:
            init += "-Q2-" + date[0]
        case 7|8|9:
            init += "-Q3-" + date[0]
        case 10|11|12:
            init += "-Q4-" + date[0]
    return init

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
        return f"{50*"-"}\nKundennummer: {self.knr}\n{self.sex}\n{self.name}\nAdresse: {self.adresse}\nLeihstatus: {self.leihstatus}\n{self.geliehen.strip()}\n"

class Bibliothek():
    def __init__(self):
        self.modus = ""
        self.pathMedia = "media.csv"
        self.pathKunde = "customer.csv"
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
        # Feldnamen für die CSV-Datei
        fieldnames = ["ID", "Typ", "Autor", "Titel", "Status", "Rueckgabe", "LetzterNutzer"]
        # Datei öffnen und DictWriter erstellen
        with open('media_output.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            # Header schreiben
            writer.writeheader()
            # Daten schreiben
            for media in self.catMedia:
                writer.writerow({
                    "ID": media.id,
                    "Typ": media.typ,
                    "Autor": media.autor,
                    "Titel": media.titel,
                    "Status": media.status,
                    "Rueckgabe": media.r_datum,
                    "LetzterNutzer": media.letzterNutzer
                })
        print("Medien-Datei wurde aktualisiert.")
    def saveKundeToCSV(self):
        # Feldnamen für die CSV-Datei
        fieldnames = ["name","sex","address","cID","leihstatus","gelieheneMedien"]
        # Datei öffnen und DictWriter erstellen
        with open('cust_output.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            # Header schreiben
            writer.writeheader()
            # Daten schreiben
            for k in self.regKunde:
                writer.writerow({
                    "name": k.name,
                    "sex": k.sex,
                    "address": k.adresse,
                    "cID": k.knr,
                    "leihstatus": k.leihstatus,
                    "gelieheneMedien": k.geliehen,
                })
        print("Kunden-Datei wurde aktualisiert.")
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
                    if m.r_datum != "" and m.r_datum < make_date():
                        print(m)            
    def newMedia(self):
        id = input("Bitte Medien ID eingeben:\n")
        typ = input("Bitte Medientyp eingeben:\n")
        autor = input("Bitte Autor/ Künstler eingeben:\n")
        titel = input("Bitte Titel eingeben:\n")
        self.catMedia.append(Media(id, typ, autor, titel, "verfügbar","",""))
        print(f"{typ} wurde hinzugefügt:\n", self.catMedia[-1])
    def extendMedia(self):
        mediaID = input("Bitte Medien ID eingeben:\n")
        newDate = make_date(int(input("Neue Dauer (Tage) ab heutigen Tag eingeben: ")))
        for m in self.catMedia:
            if m.id == mediaID:
                m.r_datum = newDate
                print(f"Leihe wurde verlängert bis {newDate}")
    def searchCust(self):
        c_id = input("Bitte Kundennummer eingeben: ")
        for k in self.regKunde:
            if k.knr.replace(" ","") == c_id:
                print(k)
                return k
    def newCust(self):
        name = input("Bitte Namen eingeben:\n")
        knr = make_cID(name)
        sex = input("Bitte Anrede eingeben: ")
        adresse = input("Bitte Adresse eingeben:\n")
        self.regKunde.append(Kunde(name,sex,adresse,knr,"inaktiv", ""))
        print("Kunde wurde registriert:\n", self.regKunde[-1])
    def fetchCustLoans(self, kunde):
            return kunde.geliehen.replace(" ","").split(",")    
    def checkLate(self,m_id):
        for m in self.catMedia:
            if m.id == m_id:
                if m.r_datum < make_date():
                    print("Verspätete Rückgabe:\n",m)
                    return True
                else: return False
    def inMedia(self):
        customer = self.searchCust()
        loans = self.fetchCustLoans(customer)
        late = False
        for m_id in loans:
            if self.checkLate(m_id):
                late = True
        run_mod = "j"
        while len(loans)>0:
                #while run_mod == "j":
                # if run_mod == "j":
                run_mod = input("Rückgabe fortsetzen? j/n ")
                if run_mod == "j":
                    media_id = input("Bitte Medien ID eingeben: ")
                    for m in self.catMedia:
                        if m.id == media_id:
                            m.status = "verfügbar"
                            m.r_datum = ""
                            m.letzterNutzer = customer.knr
                            loans.remove(media_id)
                            customer.geliehen = ",".join(loans)
                else: break
        if len(loans) == 0: 
            customer.leihstatus = "inaktiv"
            print(f"\n{customer.name} hat alle Medien zurückgegeben.")
        else: print(f"\n{customer.name} hat noch weitere Medien.")
    def outMedia(self):
        customer = self.searchCust()
        loans = self.fetchCustLoans(customer)
        late = False
        for m_id in loans:
            if self.checkLate(m_id):
                late = True
                break
        run_mod = "j"
        while run_mod == "j":
            run_mod = input("Verleih fortsetzen? j/n ")
            if run_mod == "j":
                media_id = input("Bitte Medien ID eingeben: ")
                for m in self.catMedia:
                    if m.id == media_id:
                        m.status = "verliehen"
                        m.r_datum = make_date(int(input("Verleihdauer in Tagen: ")))
                        customer.leihstatus = "aktiv"
                        customer.geliehen += f",{media_id}"
    def terminate(self):
        self.saveMediaToCSV()
        self.saveKundeToCSV()
        print("Programm wurde beendet!")
    def dialog(self):      
        while self.modus != "x":
            print("""
            Welche Aufgabe soll erledigt werden?
                  
            1   Verleih Medium
            2   Rückgabe Medium
            3   Anzeige aller Medien
            4   Suche Medium
            5   Neues Medium
            6   Leihdauer verlängern
            7   Anzeige aller Kunden
            8   Suche Kunde
            9   Neuer Kunde
            x   Programm beenden                 
                  """)
            self.modus = input("Eingabe: ")
            match self.modus:
                case "1":
                    self.outMedia()
                case "2":
                    self.inMedia()
                case "3":
                    self.showAllMedia()
                case "4":
                    self.searchMedia()
                case "5":
                    self.newMedia()
                case "6":
                    self.extendMedia()
                case "7":
                    self.showAllCustomers()
                case "8":
                    self.searchCust()
                case "9":
                    self.newCust()
                case "x":
                    self.terminate()


if __name__ == '__main__':
    bib = Bibliothek()