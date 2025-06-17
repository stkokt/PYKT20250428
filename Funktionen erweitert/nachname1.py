# Aufgabe: 
# Implementiere eine Funktion, welche den Nachnamen einer Person zurückliefert.
# Vereinfachung: Als Nachname zählt das letzte Wort eines vollständigen Namens

# Lösung: Anfang
def surname(name: str):
    return name.split(" ")[-1]
# Lösung: Ende

print(surname("Kaisley Cherry")) # Ausgabe: Cherry
print(surname("Rome Turner")) # Ausgabe: Turner


# -----------------------------------
# Aufgabe: 
# Nutze die Sortierfunktion sorted um die folgende Liste alphabtisch nach den Nachnamen zu sortieren.
# Hinweis: Verwende die Funktion surname
personen = ["Kaisley Cherry", "Rome Turner", "Brooklyn English", "Junior Novak","Kaiya Bullock"]

# Lösung: Anfang
print(sorted(personen, key=surname))
# Lösung: Ende


# -----------------------------------
# Aufgabe: 
# Verwende anstatt der Funktion surname ein Lambda

# Lösung: Anfang
print(sorted(personen, key= lambda name: name.split(" ")[-1]))
# Lösung: Ende