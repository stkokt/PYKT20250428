# Aufgabe:
# Implementiere die Funktion "rechner". Diese bildet die Summe, das Produkt oder den Durchschnitt einer beliebig langen Zahlensequenz.
# Der Aufruf der Funktion "rechner" ist mit Beispielargumenten ist vorgegeben.

# Lösung: Anfang
def rechner(operation, *zahlen):
    match operation:
        case "+": 
            summe = 0
            for zahl in zahlen:
                summe += zahl
            return summe

        case "*": 
            product = 1
            for zahl in zahlen:
                product *= zahl
            return product

        case "⌀": 
            summe = 0
            for zahl in zahlen:
                summe += zahl
            return summe / len(zahlen)
# Lösung: Ende

# Beispielaufrufe:
print(rechner("+", 1, 2, 3, 4, 5)) # Ausgabe der Summe von 15
print(rechner("*", 1, 2, 3, 4, 5)) # Ausgabe des Produkts von 120
print(rechner("⌀", 1, 2, 3, 4, 5)) # Ausgabe des Durchschnitts von 3
