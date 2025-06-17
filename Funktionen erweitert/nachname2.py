# Aufgabe:
# Nutze die Sortierfunktion sorted um die folgende Liste nach der Länge der Nachnamen zu sortieren.
personen = ["Kaisley Cherry", "Rome Turner", "Brooklyn English", "Junior Novak","Kaiya Bullock"]

# Lösung: Anfang
def surname_length(name: str):
    return len(name.split(" ")[-1])

print(sorted(personen, key=surname_length))
# Lösung: Ende