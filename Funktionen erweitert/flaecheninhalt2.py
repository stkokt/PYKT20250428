# Aufgabe:
# Implementiere die Funktion "flaecheninhalt"
# Bekommt die Funktion ein Argument übergeben, berechnet sie den Flächeninhalt eines Quadrats
# Bekommt die Funktion zwei Argumente übergeben, berechnet sie den Flächeninhalt eines Rechtecks
# Bekommt die Funktion mehr als zwei oder keine Argumente übergeben, gibt sie eine Fehlermeldung aus
# Hinweis: Verwende die Möglichkeit Argumente als Listen zu übergeben

# Lösung: Anfang
def flaecheninhalt(*zahlen: list):
    match len(zahlen):
        case 1:
            return zahlen[0] * zahlen[0]
        case 2:
            return zahlen[0] * zahlen[1]
        case _:
            print("Bitte nur ein oder zwei Argumente angeben!")
# Lösung: Ende

# Beispielaufrufe:
print(flaecheninhalt(12))          # gibt 144 aus
print(flaecheninhalt(12, 10))      # gibt 120 aus
#print(flaecheninhalt(12, 10, 20)) # gibt einen Fehler aus