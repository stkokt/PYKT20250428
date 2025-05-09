#Aufgabe 1: Schreibe ein Programm, das das Alter 
#           eines Benutzers einliest und die
#           Altersgruppen wie folgt klassifiziert:
#           - Kind: 0-12
#           - Teenager: 13-19
#           - Erwachsener: 20-64
#           - Senior: 65+


# Aufgabe 2: Schreibe ein Programm, das eine Zahl 
#            zwischen 1 und 7 einliest und den 
#            entsprechenden Wochentag ausgibt.


# Aufgabe 3: Schreibe ein Programm, das eine Note 
#            zwischen 1 und 6 einliest und die 
#            entsprechende Bewertung ausgibt:
#            - 1: Sehr gut
#            - 2: Gut
#            - 3: Befriedigend
#            - 4: Ausreichend
#            - 5: Mangelhaft
#            - 6: Ungenügend


# Aufgabe 4: Schreibe ein Programm, das den Namen 
#            eines Monats einliest und die Anzahl 
#            der Tage in diesem Monat ausgibt.


# Aufgabe 5: Schreibe ein Programm, das das Gewicht (in kg) 
#            und die Größe (in m) eines Benutzers einliest und 
#            den BMI berechnet. Klassifiziere den BMI wie folgt:
#            - Untergewicht: BMI < 18.5
#            - Normalgewicht: 18.5 <= BMI < 25
#            - Übergewicht: 25 <= BMI < 30
#            - Adipositas: BMI >= 30


# Aufgabe 6: Schreibe ein Programm, das das 
#            Einkommen eines Benutzers einliest 
#            und die Steuer wie folgt berechnet:
#            - Einkommen < 10000: 0% Steuer
#            - 10000 <= Einkommen < 30000: 10% Steuer
#            - 30000 <= Einkommen < 50000: 20% Steuer
#            - Einkommen >= 50000: 30% Steuer


# Aufgabe 7: Schreibe ein Programm, das zwei 
#            Farben einliest und die resultierende 
#            Farbe ausgibt, wenn sie gemischt werden:
#            - Rot + Blau = Lila
#            - Rot + Gelb = Orange
#            - Blau + Gelb = Grün
#            - Andere Kombinationen: Unbekannt


# Aufgabe 8: Schreibe ein Programm, das den 
#             Namen eines Monats einliest und 
#             die entsprechende Jahreszeit ausgibt.

# Frühjahr: März - inkl. Mai, Sommer: Juni - inkl. August, 
# Herbst: September - inkl. November, Winter: Dezember bis inkl. Februar

# Aufgabe 9: Schreibe ein Konsolenmenu, über das du 
#            eine der oben stehenden Aufgaben anwählen kannst.


loop = ""
while loop != "x":
    print("""
          Gebe einen Buchstaben ein:

          a: Aufgabe 1        e: Aufgabe 5        x: Beenden
          b: Aufgabe 2        f: Aufgabe 6
          c: Aufgabe 3        g: Aufgabe 7
          d: Aufgabe 4        h: Aufgabe 8          
          """)
    loop = input("Deine Eingabe:\n")
    match loop:
        case "a": 
            alter = int(input("Gib dein Alter ein: "))

            if alter <= 12:
                print("Kind")
            elif 13 <= alter <= 19:
                print("Teenager")
            elif 20 <= alter <= 64:
                print("Erwachsener")
            else:
                print("Senior")

        case "b":
            tag = int(input("Gib eine Zahl zwischen 1 und 7 ein: "))

            match tag:
                case 1:
                    print("Montag")
                case 2:
                    print("Dienstag")
                case 3:
                    print("Mittwoch")
                case 4:
                    print("Donnerstag")
                case 5:
                    print("Freitag")
                case 6:
                    print("Samstag")
                case 7:
                    print("Sonntag")
                case _:
                    print("Ungültige Eingabe")

        case "c":

            note = input("Gib eine Note zwischen 1 und 6 ein: ")

            match note:
                case "1":
                    print("Sehr gut")
                case "2":
                    print("Gut")
                case "3":
                    print("Befriedigend")
                case "4":
                    print("Ausreichend")
                case "5":
                    print("Mangelhaft")
                case "6":
                    print("Ungenügend")
                case _:
                    print("Ungültige Eingabe")

        case "d":

            monat = input("Gib den Namen eines Monats ein: ").lower().strip()

            match monat:
                case "januar" | "märz" | "mai" | "juli" | "august" | "oktober" | "dezember":
                    print("31 Tage")
                case "april" | "juni" | "september" | "november":
                    print("30 Tage")
                case "februar":
                    print("28 oder 29 Tage")
                case _:
                    print("Ungültige Eingabe")

        case "e":

            gewicht = float(input("Gib dein Gewicht in kg ein: "))
            groesse = float(input("Gib deine Größe in m ein: "))
           
            bmi = gewicht / (groesse ** 2)

            if bmi < 18.5:
                print("Untergewicht")
            elif 18.5 <= bmi < 25:
                print("Normalgewicht")
            elif 25 <= bmi < 30:
                print("Übergewicht")
            else:
                print("Adipositas")

        case "f":

            einkommen = float(input("Gib dein Einkommen ein: "))

            if einkommen < 10000:
                steuer = 0
            elif 10000 <= einkommen < 30000:
                steuer = einkommen * 0.1
            elif 30000 <= einkommen < 50000:
                steuer = einkommen * 0.2
            else:
                steuer = einkommen * 0.3

            print(f"Die Steuer beträgt: {steuer}")

        case "g":

            farbe1 = input("Gib die erste Farbe ein: ").lower()
            farbe2 = input("Gib die zweite Farbe ein: ").lower()

            if (farbe1 == "rot" and farbe2 == "blau") or (farbe1 == "blau" and farbe2 == "rot"):
                print("Lila")
            elif (farbe1 == "rot" and farbe2 == "gelb") or (farbe1 == "gelb" and farbe2 == "rot"):
                print("Orange")
            elif (farbe1 == "blau" and farbe2 == "gelb") or (farbe1 == "gelb" and farbe2 == "blau"):
                print("Grün")
            else:
                print("Unbekannt")

        case "h":

            monat = input("Gib den Namen eines Monats ein: ").lower().strip()

            match monat:
                case "dezember" | "januar" | "februar":
                    print("Winter")
                case "märz" | "april" | "mai":
                    print("Frühling")
                case "juni" | "juli" | "august":
                    print("Sommer")
                case "september" | "oktober" | "november":
                    print("Herbst")
                case _:
                    print("Ungültige Eingabe")

        case _:
            continue
