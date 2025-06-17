# Aufgabe:
# Implementiere die Funktion "durchschnitt", welche das arithmetische Mittel (den Durchschnitt) berechnet. 
# Die Funktion kann beliebig viele Zahlen übergeben bekommen.

# Lösung: Anfang
def durchschnitt(*zahlen: list) -> float:
    summe = 0
    for zahl in zahlen:
        summe += zahl

    return summe / len(zahlen)
# Lösung: Ende

# Beispielaufruf:
print(durchschnitt(1,2,3,4,5,6,7,8,9)) # gibt 5.0 aus
