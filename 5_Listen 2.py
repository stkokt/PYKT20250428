# Aufgabe 1: Durchlaufe die Liste und gebe jeden Wert an einem geraden Index aus.

print("\nAufgabe1\n")

liste = [68, 52, 92, 60, 54, 4, 50, 9, 67] 

for idx, zahl in enumerate(liste):
    if idx%2==0:
        print(zahl, end=" ")


# Aufgabe 2: Schreibe eine Liste von Listen in eine einfache Liste um.
#            Nutze dazu zwei verschachtelte For- Loops
print("\n\nAufgabe2\n")

liste_von_listen = [[1,2,3], [4,5,6], [7,8,9]]

flache_liste = [] # [1,2,3,4,5,6,7,8,9]

# Alternative 1
for sublist in liste_von_listen:
    for zahl in sublist:
        flache_liste.append(zahl)

print(flache_liste)

flache_liste = []

# Alternative 2
for sublist in liste_von_listen:
    flache_liste.extend(sublist)

print(flache_liste)

# Aufgabe 3:

print("Aufgabe 3")
 

"""
Muster aus Zahlen ausgeben:
Schreibe ein Programm, das folgendes Muster ausgibt:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Verwende eine Schleife, um das Muster zu erstellen.
"""
print("\nAufgabe3\n")

# Alternative 1
cnt = 1
while cnt < 6:
    for zahl in range(1,cnt+1):
        print(zahl, end=" ")
    cnt+=1
    print()

# Alternative 2
cnt = 0
liste_triangle = [1,2,3,4,5]

while cnt < len(liste_triangle):
    print(*liste_triangle[:cnt+1:])
    cnt+=1

# Alternative 3
for zeile in range(0,6):
    for zahl in range(1,zeile+1):
        print(zahl, end=" ")
    print()

# Alternative 4
for zahl in range(1,6):
    for zeile in range(1,zahl+1):
        print(zeile,end=' ')
    print()
 

# Aufgabe 4: Schreibe die liste_of_5 so, dass statt einer durch 5 teilbaren Zahl aus liste_0_100 eine Liste eingefügt wird, 
# die alle bis dorthin durch 5 teilbaren Zahlen enthält. Also: [[0],1,2,3,4,[0,5],6,7,8,9,[0,5,10]...

liste_0_100 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
liste_of_5 = []

tmp_list = []
for zahl in liste_0_100:
    if zahl % 5 == 0:
        tmp_list.append(zahl)
        liste_of_5.append(tmp_list.copy())
    else:
        liste_of_5.append(zahl)

print(liste_of_5)
# for elem in liste_of_5:
#     if type(elem) == list:
#         print(id(elem))



# Aufgabe 5: Gebe Zahlen bis inklusive n aus.
#            Nutze dafür die liste_n und die darin enthaltenen Zahlen.
#            Tipp: Zwei verschachtelte Loops.
#            0 1 2 3 
#            0 1 2 3 4 5 
#            0 1 2 3 4 5 6 7 

liste_n = [3,5,7]
for n in liste_n:
    for zahl in range(n+1):
        print(zahl,end=" ")
    print()


# Aufgabe 6: Personen innerhalb einer Liste suchen
"""
Vorgegeben:

Liste mit Namen

Hinweis:
for-Schleife
if-Bedingung
String-Methode: startwith(...)
Variablen

Aufgabenteil a:
Eingabe: Exakter Name
Ausgabe: Alle Einträge die passen
Aufgabenteil b:
Eingabe: Anfang eines Namens
Ausgabe: Alle Einträge die passen
Aufgabenteil c:
Eingabe: Anfang eines Namens
Ausgabe: Maximal die ersten drei passenden Einträge
Aufgabenteil d:
Eingabe: Ein Nachname
Ausgabe: Index des Listenelements
-----------------------------
"""
namen = ["Levi Schneider","Lina Schmitt","Emil Weber","Liam Fischer","Lia Krause",
         "Emilia Hartmann","Anton Meyer","Theo Wagner","Emma Koch","Paul Becker",
         "Leano Schulz","Elias Richter","Jakob Hofmann","Ella Herrmann",
         "Ida Schröder","Samuel Braun","Laura Stein"]

suche_a = "Paul Becker"
suche_b = "Li"
suche_c = "L"
suche_d = "Schröder"

# Aufgabenteil a
gefunden = False

for name in namen:
    if name==suche_a:
        print(f"Name '{suche_a}' gefunden")
        gefunden = True
if gefunden == False:
    print(f"Name '{suche_a}' nicht gefunden")

# Aufgabenteil b
gefunden = False

for name in namen:
    if name.startswith(suche_b):
        print(f"Name beginnend mit '{suche_b}' gefunden: {name}")
        gefunden = True
if gefunden == False:
    print(f"Name beginnend mit '{suche_b}' nicht gefunden")

# Aufgabenteil c
gefunden = False
search2list=[]

for name in namen:
    if name.startswith(suche_c):
        search2list.append(name)
        gefunden = True
if gefunden == False:
    print(f"Name beginnend mit '{suche_c}' nicht gefunden")
if gefunden:
    for name in search2list[0:3]: 
        print(name)

# List- Slicing
# print([1,2,3,4,5,6][:-1])
# print("Hello"[1:4])

# Aufgabenteil d
gefunden = False

for index, name in enumerate(namen):
    if name.endswith(suche_d):
        print(f"Name wurde gefunden am Index {index}.")
        gefunden = True
if gefunden == False:
    print(f"Nachname '{suche_d}' nicht gefunden")

# Aufgabe 7: Gibt es in der Liste neg_pos mehr negative
#            oder mehr positive Zahlen?

neg_pos = [25, -8, -44, -41, 29, -4, 13, -42, -21, 34]
cnt = 0
for zahl in neg_pos:
    if zahl > 0:
        cnt+=1
    if zahl < 0:
        cnt-=1

print("Mehr negative") if cnt<0 else print("Mehr positive")
# a<b?a:b    # in z.B. C++: ist a kleiner b, wenn ja, nimm a, ansonsten b

anz_pos = len([z for z in neg_pos if z > 0])
anz_neg = len([z for z in neg_pos if z < 0])