"""
Methoden des Datentyps 'list':

 1  append(self, object, /)
 |      Append object to the end of the list.
 |
 2  clear(self, /)
 |      Remove all items from list.
 |
 3  copy(self, /)
 |      Return a shallow copy of the list.
 |
 4  count(self, value, /)
 |      Return number of occurrences of value.
 |
 5  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |
 6  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 7  insert(self, index, object, /)
 |      Insert object before index.
 |
 8  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |
 |      Raises IndexError if list is empty or index is out of range.
 |
 9  remove(self, value, /)
 |      Remove first occurrence of value.
 |
 |      Raises ValueError if the value is not present.
 |
 10 reverse(self, /)
 |      Reverse *IN PLACE*.
 |
 11 sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |
 |      The reverse flag can be set to sort in descending order.

"""


listeA = [15, 7, 39, 13, 41, 21, 20, 4, 13, 
          16, 40, 28, 45, 12, 19, 10, 28, 36, 
          48, 14, 30, 3, 37, 26, 21, 1, 33, 33, 10, 11]
print(len(listeA))

# Aufgabe 1: Durchlaufe die Liste A mit einem For- Loop
#            und gebe sie damit aus.

print("\nAufgabe 1\n")

# Alternativ: for zahl in listeA:
#                print(zahl, end=" ")
for zahl in range(len(listeA)):
    print(listeA[zahl], end=" ")


# Aufgabe 2: Gebe nur das erste und das letzte Element
#            der Liste A aus.

print("\nAufgabe 2\n")

# Alternativ: print(listeA[0], listeA[len(listeA)-1])
print(listeA[0], listeA[-1])

# Aufgabe 3: Gebe nur die geradzahligen Elemente
#            der Liste A aus.

print("\nAufgabe 3\n")

for zahl in range(len(listeA)): # 0,1,2,3,....,29
    if listeA[zahl] % 2 == 0:
        print(listeA[zahl], end=" ")

# Vorsicht:
    # if listeA[zahl] % 2:
    #     print(listeA[zahl], end=" ")
# gibt die ungeraden Zahlen aus

# Aufgabe 4: Ermittle und gebe aus, wieviele Elemente
#            die Liste A enthält.

print("\nAufgabe 4\n")

print(f"Anzahl der Elemente: {len(listeA)}.")

# Aufgabe 5: Gebe die Liste in der Form aus:
#            "Das 1. Element ist 15"
#            "Das 2. Element ist 7" usw.

print("\nAufgabe 5\n")

for index, zahl in enumerate(listeA):
    print(f"Das {index + 1}. Element ist {zahl}")

# Aufgabe 6: Zähle die geraden und die ungeraden Zahlen
#            und gebe die jeweilige Anzahl aus.
#            Erhöhter Schwierigkeitsgrad: Nutze dafür nur eine(!)
#            Zählvariable.

print("\nAufgabe 6\n")

cntList = [0,0]
for zahl in listeA:
    if zahl % 2 == 0:
        cntList[0] += 1
    else:
        cntList[1] += 1
print(f"Es gibt {cntList[0]} gerade und {cntList[1]} ungerade Zahlen in listeA.")

# Aufgabe 7: Gebe die Liste A bis zur Hälfte aus.
#            (Letztes Element: 19)

print("\nAufgabe 7\n")

for zahl in range((len(listeA)//2)):
    print(listeA[zahl], end=" ")


# Aufgabe 8: Gebe die Liste A ab der Hälfte aus.
#            (Erstes Element: 10)

print("\nAufgabe 8\n")

for zahl in range((len(listeA)//2), len(listeA)):
    print(listeA[zahl], end=" ")


# Aufgabe 9: Gebe alle Elemente der Liste A aus, 
#            die an einem geradzahligen Index stehen.

print("\nAufgabe 9\n")

for index, zahl in enumerate(listeA):
    if index % 2 == 0:
        print(zahl, end = " ")

# Aufgabe 10: Gebe das größte und das kleinste Element 
#             der Liste A aus, sowie die Summe
#             und den Durchschnitt aller Listenelemente.

print("\nAufgabe 10\n")

print(f"Größtes Element: {max(listeA)}, kleinstes Element: {min(listeA)}")




