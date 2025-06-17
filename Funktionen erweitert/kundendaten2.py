# Sortierfunktion, die den Bubblesort Algorithmus umsetzt
# Weitere Infors unter: https://de.wikipedia.org/wiki/Bubblesort
def bubblesort(mylist, comparefct: callable):
    for _ in range(len(mylist)):
        for index in range(len(mylist)-1):
            if comparefct(mylist[index], mylist[index+1]):
                # Alternative 1:
                mylist[index], mylist[index+1] = mylist[index+1], mylist[index]
                # Alternative 2:
                # temp = mylist[index+1]
                # mylist[index+1] = mylist[index]
                # mylist[index] = temp

# Beispielverwendung der Sortierfunktion:
def aufsteigend(x, y):
    return x > y

zahlen = [6,2,7,9,10]
bubblesort(zahlen, aufsteigend)
print(zahlen)

# -----------------------------------

kundendaten = [
    {"vorname": "Rome",     "nachname": "Turner",  "bundesland": "Bayern"},
    {"vorname": "Brooklyn", "nachname": "English", "bundesland": "NRW"},
    {"vorname": "Junior",   "nachname": "Novak",   "bundesland": "Berlin"},
    {"vorname": "Kaiya",    "nachname": "Bullock", "bundesland": "Sachsen"},
    {"vorname": "Kaisley",  "nachname": "Cherry",  "bundesland": "NRW"}
]

def kundeninfo(kundendaten):
    for kunde in kundendaten:
        print(f"Vorname: {kunde["vorname"]:<10} Nachname: {kunde["nachname"]:<10} Bundesland: {kunde["bundesland"]:<10}")


# -----------------------------------
# Aufgabe: Sortiere die Kundendaten nach dem Vornamen 
# Lösung: Anfang
def vorname(x, y):
    return x['vorname'] > y['vorname']
# Lösung: Ende
bubblesort(kundendaten, vorname)
kundeninfo(kundendaten)
print("---------------------------")


# -----------------------------------
# Aufgabe: Sortiere die Kundendaten zuerst nach dem Bundesland und innerhalb eines jeden Bundeslandes nach dem Vornamen der Kunden
# Lösung: Anfang
# def bundesland_vor_nachname(x, y):
#     if x['bundesland'] != y['bundesland']:
#         return x['bundesland'] > y['bundesland']
#     else:
#        return x['vorname'] > y['vorname']
    
def bundesland_vor_nachname(x, y):
    if x['bundesland'] == y['bundesland']:
        return x['vorname'] > y['vorname']
    else:
        return x['bundesland'] > y['bundesland']

# Lösung: Ende
bubblesort(kundendaten, bundesland_vor_nachname)
kundeninfo(kundendaten)
print("---------------------------")
