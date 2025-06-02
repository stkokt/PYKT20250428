kleinbuchstaben = "qwertzuiopasdfghjklyxcvbnm"  # Wasims Variante

# In Bezug auf die ASCII- Tabelle, in der die Kleinbuchstaben
# den Dezimalzahlen von 97 bis 122 entsprechen:
# In der List- Comprehension werden die Zahlen zu einem
# Character konvertiert.
# Die Liste wird dann an einen leeren String gejoint.
klein = "".join([chr(char) for char in range(97, 123)])
# print(klein)

# Die Sonderzeichen stehen in getrennten Bereichen der ASCII- Tabelle,
# daher werden im Folgenden zwei Listen aus unterschiedlichen Ranges konkatiniert
sonder = [chr(num) for num in list(range(33,45)) + list(range(58,65))]
# print(type(sonder))
# print(sonder)
# sonder1 = list(chr(i for i in range(33,45)))
# print(sonder1)

# DICTIONARY

# Ein leeres Dictionary erstellen
a_dict = {} # alternativ: = dict()
# Einen Eintrag hinzufügen
a_dict["Vorname"] = "Stefan"
a_dict.update({"Nachname": "Koschnik"})
a_dict |= {"Alter":55}  # bitwise Oder

#   0001
#   0010  |
#   0011

# print(a_dict)
a_dict2 = {}
# Übertragen der Keys eines anderen Dictionarys
a_dict2 = a_dict2.fromkeys(a_dict)
# print(a_dict2)
# print(a_dict2.get("Vorname"))

# dict().fromkeys() zum Entfernen von Duplikaten
# unetr Beibehaltung der Reihenfolge
liste = [1,2,1,5,4,5,6]
# Hier werden zwar die Duplikate entfernt, 
# aber auch die Reihenfolge wird geändert.
# liste = set(liste)    
liste = list({}.fromkeys(liste))
# print(liste)

# Als Keys für Dictionaries können nur immutable 
# Datentypen verwendet werden, also nicht:

# L = Listen
# S = Sets
# D = Dictionaries

# denn mutable Datatypes sind unhashable
# a_dict3 = {[1,2,3]: 1} # funktioniert nicht, weil Liste nicht hashable

# dict().items(), um Zugriff sowohl auf Keys als auch Values zu haben 
for k, v in a_dict.items():
    print(f"{k} : {v}")

# Nur die Keys
print(a_dict.keys())
# Nur die Values
print(a_dict.values())

# Entfernen des letzten Items (gibt ein Tuple zurück)
print(a_dict.popitem())
print(a_dict)
print(a_dict.popitem())
print(a_dict)