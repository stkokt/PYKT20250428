de_en = {"ja": "yes", "nein": "no", "Auto": "car", "grau": "grey", "Morgen": "tomorrow", "morgen": "morning"}

run = True
while run:
    modus = input("Bitte wählen z/zz (anzeigen), u (übersetzten), n (#eintraege), e (einfügen), r (ersetzen), l (löschen), b (beenden): ")
    
    match modus:
        case "z":
           for de,en in de_en.items():
               print(de, "->", en)

        case "zz":
            # Alternative 1:
            # de_sorted = sorted(de_en.keys())
            # for de in de_sorted:
            #     en = de_en[de]
            #     print(de, "->", en)

            # Alternative 2:
            for de in sorted(de_en):
                print(de, "->", de_en[de])

        case "u":
            deutsch = input("Deutsches Wort: ")
            if deutsch in de_en:
                englisch = de_en[deutsch]
                print("Englische Übersetzung:", englisch)
            else:
                print(f"Das Wörterbuch enthält keine Übersetzung für '{deutsch}'")

        case "n":
            anzahl_eintraege = len(de_en)
            print("Das Wörterbuch hat", anzahl_eintraege, "Einträge.")
            
        case "e":
            deutsch = input("Deutsches Wort: ")
            if deutsch not in de_en:
                englisch = input("Englisches Wort: ")
                de_en[deutsch] = englisch
            else:
                print("Fehler! Eintrag bereits vorhanden")

        case "r":
            deutsch = input("Deutsches Wort: ")
            if deutsch in de_en:
                englisch = input("Englisches Wort: ")
                de_en[deutsch] = englisch
            else:
                print("Fehler! Eintrag nicht vorhanden")

        case "l":
            deutsch = input("Deutsches Wort: ")
            if deutsch in de_en:
                del de_en[deutsch]
            else:
                print("Konnte Eintrag mit Key", deutsch,"nicht entfernen, da nicht vorhanden.")
               
        case "b":
            run = False

        case _:
            print("Modus nicht unterstützt!")