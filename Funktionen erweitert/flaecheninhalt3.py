# Aufgabe:
# Implementiere die Funktion "flaecheninhalt"
# Bekommt die Funktion ein Argument übergeben, berechnet sie den Flächeninhalt eines Quadrats
# Bekommt die Funktion zwei Argumente übergeben, berechnet sie den Flächeninhalt eines Rechtecks
# Bekommt die Funktion mehr als zwei oder keine Argumente übergeben, gibt sie eine Fehlermeldung aus
# Hinweis: Verwende Parameter mit Default-Werte. Nutze den Default-Wert um zu erkennen, ob der Parameter genutzt wurde oder nicht.

# Lösung: Anfang
def flaecheninhalt(seite_a, seite_b = None):
    if seite_b == None:
        return seite_a * seite_a
    else:
        return seite_a * seite_b   
# Lösung: Ende

# Beispielaufrufe:
print(flaecheninhalt(12))          # gibt 144 aus
print(flaecheninhalt(12, 10))      # gibt 120 aus
# print(flaecheninhalt(12, 10, 20)) # gibt einen Fehler aus
