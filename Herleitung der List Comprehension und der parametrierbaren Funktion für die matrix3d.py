# Herleitung der List Comprehension und der parametrierbaren Funktion
# für die 3 x 3 x 3 Matrix:

# [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
# [[10, 11, 12], [13, 14, 15], [16, 17, 18]], 
# [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

# matrix3d_loop = []

# for i in range(3):
#     matrix3d_loop.append(i)

# print(matrix3d_loop)

print("\n1. Schritt\n")

matrix3d_loop = []
# Wir fangen ganz einfach an und lassen einen Loop mit drei 
# Durchläufen die jeweilige Nummer des Loops in die Zielmatrix schreiben.

for i in range(3):
    matrix3d_loop.append(i)

print(matrix3d_loop)    # [0, 1, 2]

print("\n2. Schritt\n")

matrix3d_loop = []

for i in range(3):
    matrix3d_loop.append(i+1)   # Wir müssen die Nummern um 1 erhöhen.

print(matrix3d_loop)    # [1, 2, 3]

print("\n3. Schritt\n")

matrix3d_loop = []
# Wir wollen Listen in die Zielliste schreiben.
# Wir brauchen also einen weiteren Loop und eine 
# temporäre Liste, in der wir die Zwischenergebnisse
# speichern, bevor wir die temporäre Liste in die Zielliste 
# schreiben und der nächste Loop diese Zwischenliste
# wieder leert.

for j in range(3):      # weiterer Loop
    liste_i = []        # temporäre Liste/ ist bei Beginn jedes Loopdurchlaufs leer
    for i in range(3):
        liste_i.append(i+1) # die Zahlen werden in die temporäre Liste geschrieben.
    matrix3d_loop.append(liste_i)   # die temporäre Liste wird in die Zielliste geschrieben

print(matrix3d_loop)    # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print("\n4. Schritt\n")

matrix3d_loop = []

for j in range(3):
    liste_i = []
    for i in range(3):
        liste_i.append(i+1+j)   # Wir müssen wieder die Zahlen manipulieren.
    matrix3d_loop.append(liste_i)

print(matrix3d_loop)

print("\n5. Schritt\n") # [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

matrix3d_loop = []

for j in range(3):
    liste_i = []
    for i in range(3):
        liste_i.append(i+1+j*3) # Die letzte Manipulation hat noch nicht genügt.
    matrix3d_loop.append(liste_i)

print(matrix3d_loop) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                     # Das ist strukturell bereits eine von drei Listen, die wir brauchen.
                     # Aber sie muss selbst in einer Liste eingebettet sein und es braucht
                     # drei davon, in denen die Zahlen weiter hoch gezählt werden.
print("\n6. Schritt\n") 

matrix3d_loop = []
# Wir brauchen also noch einen letzten Loop, die Liste aus Schritt 5
# drei mal in die Zielliste kommt. Weil sie dabei dann auch in eine weitere Liste
# eingebettet sein soll, brauchen wir also außerdem eine weitere Zwischenliste.

for k in range(3):
    liste_j = []    # + Zwischenliste liste_j
    for j in range(3):
        liste_i = []
        for i in range(3):
            liste_i.append(i+1+j*3)
        liste_j.append(liste_i)
    matrix3d_loop.append(liste_j)

print(matrix3d_loop)
# [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]


print("\nLetzter Schritt:\n")

matrix3d_loop = []
# Soweit so gut, aber wir müssen noch die Zahlen anpassen, um von 1 bis 27 zu kommen.
for k in range(3):
    liste_j = []
    for j in range(3):
        liste_i = []
        for i in range(3):
            liste_i.append(i+1+j*3+k*3*3)   # Weitere Manipulation.
        liste_j.append(liste_i)
    matrix3d_loop.append(liste_j)

print(matrix3d_loop)    # Wir sind am Ziel!
# [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]


# Übertragung in eine Listkomprehension

#              <-----------------------Zeile 101: Zielmatrix ------------------------->
#               <-----------------Zeile 104: liste_j ------------->
#                <-----Zeile 106: liste_i ----->
#                <-Zeile 108-> <---Zeile 107--->  <---Zeile 105--->  <---Zeile 103--->
matrix3d_lc = [[[i+1+j*3+k*3*3 for i in range(3)] for j in range(3)] for k in range(3)]
print(matrix3d_lc)

# Alternative Alireza:

matrix3d = [[[] for x in range(3)] for y in range(3)]
print(matrix3d) # So sieht die unbestückte Matrix aus.
for index in range(3):
        for jindex in range(3):
            for kindex in range (3):
                # Hierfür (also append) war Zeile 127 notwendig,
                # denn sonst wären keine Listen zu appenden da.
                matrix3d[index][jindex].append(index*3*3+jindex*3+kindex+1)
print(matrix3d)

# Parametrierbare Funktion:
# Wir müssen die 3en durch geeignete Parameter ersetzen.
# Da wir eine kubische Matrix haben, gibt es also die 
# Ausdehnungen in den Dimensionen i, j und k.
# Nennen wir es mal irange, jrange und krange.
# Richtig kombiniert ergibt das:

def matrix3d_fct(irange, jrange, krange):
    return [[[i+1+j*irange+k*irange*jrange for i in range(irange)] for j in range(jrange)] for k in range(krange)]

# Viel Spass beim Spielen ;)
#print(matrix3d_fct(5,7,4))

