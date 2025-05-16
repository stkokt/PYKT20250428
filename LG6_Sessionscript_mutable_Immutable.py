# Mutable/ Immutable

# Veränderbar (mutable) sind in Python nur 3 Datentypen:
"""
L = Listen
S = Sets
D = Dictionaries
"""

a = 10  # Integers sind immutable  
print(id(a))
a = 11  # Ab hier schaut a auf eine andere Speicheradresse
print(id(a))
b = 10  # Aber b schaut jetzt auf die Adresse, die a in Zeile 10 benutzte.
print(id(b))
# Ergo: Nicht Variablen werden an Speicheradressen gespeichert,
# sondern Werte

liste = [10,11]
print(id(liste[0]), id(liste[1]))
# Folgend nur Test, ob sich ein delete katastrophal auswirkt (nein)
# del liste[0]
# print(liste)
# print(b)

# Die Speicheradressen der Werte werden auch wiederwendet,
# wenn die Werte in Listen genutzt werden.
print(id(liste))
print(id(liste[0])) # Wie RAM von 'b'
print(id(liste[1])) # Wie RAM von 'a'
liste.append(3)     # Veränderung der Liste
print(id(liste))    # aber gleiche Speicheradresse für Metainformationen
liste[2]=5          # Veränderung der Liste
print(id(liste))    # aber gleiche Speicheradresse für Metainformationen

# Strings sind immutable
text = "Hallo"  
print(id(text)) # Speicheradresse von "Hallo"
text1 = "Ballo"
print(id(text)) # Speicheradresse von "Ballo"
# Aber: Speicheradresse von 'a' in beiden Variablen gleich
print(id(text[1]), id(text1[1]))
# text[0]="B"   # führt zu einem Fehler, da 'str' immutable




