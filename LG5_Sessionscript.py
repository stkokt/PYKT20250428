# Hinzufügen der Zahlen 0 - 9 zu einer leeren Liste:

# liste10 = []

# for zahl in range(10):
#     liste10.append(zahl)

# print(liste10)

liste10 = [zahl for zahl in range(10)]

print(liste10)

# Hinzufügen nur der geraden Zahl von 0 - 9

liste_even = [] # 0,2,4,6,8

for zahl in range(10):
    if zahl%2==0:
        liste_even.append(zahl)

print(liste_even)

liste_even = [zahl for zahl in range(10) if zahl%2==0]
liste_even = [zahl for zahl in range(0,10,2)]

print(liste_even)

# Hinzufügen aller ungeraden Zahlen aus 'liste10'

liste_odd = [] # 1,3,5,7,9

for zahl in liste10:
    if zahl%2==1:
        liste_odd.append(zahl)

print(liste_odd)

liste_odd = [zahl for zahl in liste10 if zahl%2==1]

print(liste_odd)

# Hinzufügen des Dreifachen einer durch 3 teilbaren Zahl
# und des Doppelten einer geraden Zahl
# und des Einfachen einer ungeraden Zahl aus liste10:

liste23 = []

for zahl in liste10:
    if zahl%3==0:
        liste23.append(zahl*3)
    elif zahl%2==0:
        liste23.append(zahl*2)
    else:
        liste23.append(zahl)

print(liste23)

liste23 = [zahl*3 if zahl%3==0 else zahl*2 if zahl%2==0 else zahl for zahl in liste10]

# Zufallszahlen
# import random
from random import sample
liste_zufall = sample(range(1,101),10)
print(liste_zufall)


liste_verschachtelt = [[1,2], [3,4]]
print(liste_verschachtelt[0][1]) # Ergebnis: 2
print(liste_verschachtelt[1][0]) # Ergebnis: 3