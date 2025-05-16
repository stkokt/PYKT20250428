# LIST COMPREHENSIONS
# Benutze List Comprehensions zur Lösung der folgenden Aufgaben.

# SYNTAX
# zw = zielwert, bw = bezugswert, 
# bb = bezugsbereich, vgl = vergleichsausdruck

# einfach =[zw for bw in bb]
# mit_if = [zw for bw in bb if vgl]
# mit_if_else = [zw if vgl else zw2 for bw in bb]
# mit_if_else_verkettet = [zw if vgl else zw2 if vgl2 else zw3 for bw in bb]


# Aufgabe 1: Erstelle eine Liste mit jeder dritten Zahl von 1 bis 30.

print("\nAufgabe 1\n")

each3rd = [zahl for zahl in range(1, 30, 3)]
print(each3rd)  # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

# Aufgabe 2: Filtere aus der random_liste 
#            die ungeraden Zahlen in eine neue Liste.

print("\nAufgabe 2\n")

random_liste = [28, 28, 48, 86, 86, 23, 52, 14, 6, 54, 33, 24, 75, 69]
odds = [zahl for zahl in random_liste if zahl % 2 != 0]
print(odds)     # [23, 33, 75, 69]

# Aufgabe 3: Filtere aus der random_liste
#            die Zahlen, die durch 2 und 3 teilbar sind.

print("\nAufgabe 3\n")

mod2_3 = [zahl for zahl in random_liste if zahl % 2 == 0 and zahl % 3 == 0]
print(mod2_3)   # [48, 6, 54, 24]

# Aufgabe 4: Schreibe die Absolutwerte der Liste neg_pos
#            in die Liste abs_neg_pos.

print("\nAufgabe 4\n")

neg_pos = [25, -8, -44, -41, 29, -4, 13, -42, -21, 34]
abs_neg_pos = [abs(zahl) for zahl in neg_pos]
print(abs_neg_pos)  # [25, 8, 44, 41, 29, 4, 13, 42, 21, 34]

# Aufgabe 5: Die Liste sum_sumAbs_neg_pos soll zwei Werte enthalten, 
#            die Summe aller Zahlen der Liste neg_pos und die Summe
#            all derer Absolutwerte.

print("\nAufgabe 5\n")

sum_sumAbs_neg_pos = [sum(neg_pos), sum([abs(zahl) for zahl in neg_pos])]
print(sum_sumAbs_neg_pos)   # [-59, 261]

# Aufgabe 6: Die Liste one_or_zero soll eine 1 für jeden Wert >= 0
#            und eine 0 für jeden Wert < 0 in der Liste neg_pos enthalten.

print("\nAufgabe 6\n")

neg_pos = [25, -8, -44, -41, 29, -4, 13, -42, -21, 34]
one_or_zero = [0 if zahl < 0 else 1 for zahl in neg_pos ]
# All()/ANY() 
# print(all(one_or_zero))
# print(any(one_or_zero))
print(one_or_zero)  # [1, 0, 0, 0, 1, 0, 1, 0, 0, 1]

# Aufgabe 7: Die Liste words_with_a soll die Worte aus words
#            enthalten, in denen der Buchstabe 'a' ist.

print("\nAufgabe 7\n")

words = ["apple", "banana", "cherry"]
words_with_a = [word for word in words if 'a' in word]
print(words_with_a) # ['apple', 'banana']

# Aufgabe 8: Die Liste words_gt_5 soll die Worte aus words
#            enthalten, die länger als 5 Buchstaben sind.

print("\nAufgabe 8\n")

words_gt_5 = [word for word in words if len(word) > 5]
print(words_gt_5)   # ['banana', 'cherry']

# Aufgabe 9: Die Liste vok_kon soll für jedes Wort aus words
#            eine Liste enthalten, deren erster Wert die 
#            Anzahl der Vokale ("aeiou") ist und deren zweiter 
#            Wert die Anzahl der Konsonaten.
        
print("\nAufgabe 9\n")

vok_kon = [[len([char for char in word if char in "aeiou"]), len([char for char in word if char not in "aeiou"])] for word in words]
print(vok_kon)      # [[2, 3], [3, 3], [1, 5]]

# Aufgabe 10: Die Liste schmidts_idx soll die Indizes all der Namen in namen
#             enthalten, deren Nachname Schmidt ist.

print("\nAufgabe 10\n")

namen = ['Anna Müller', 'Max Schmidt', 'Lena Müller', 'Tom Schmidt', 'Sophie Müller', 'Jonas Schmidt', 'Emma Müller', 'Leo Schmidt', 'Lisa Müller', 'Finn Schmidt']
schmidts_idx = [index for index, name in enumerate(namen) if name.endswith("Schmidt")]
print(schmidts_idx) # [1, 3, 5, 7, 9]

# Aufgabe 11: Die Liste schmidts soll mit Hilfe der Liste schmidts_idx alle Namen
#             aus der Liste Namen enthalten, deren Nachname Schmidt ist.

print("\nAufgabe 11\n")

schmidts = [namen[idx] for idx in schmidts_idx]
print(schmidts) # ['Max Schmidt', 'Tom Schmidt', 'Jonas Schmidt', 'Leo Schmidt', 'Finn Schmidt']

# Aufgabe 12: Spiele Lotto (6 aus 49)! Simuliere die Ziehungen und wahlweise auch
#             den Tippschein mit einer geeigneten Methode aus dem random- Modul.

import random

print("\nAufgabe 12\n")

lostrommel = [n for n in range(1,50)]   # Liste 1 - 49
tippschein = [3,20,46,7,33,15]          # fester Tippschein
ziehung = random.sample(lostrommel, 6)  # Simulierte Ziehung

treffer_cnt = 0   # Zählt hoch, wenn eine Zahl des Tippscheins auch in der Ziehung ist.

for lottozahl in ziehung:   # Loop durch die Zahlen der Ziehung...
    if lottozahl in tippschein: # ...und Vergleich mit Tippschein.
        treffer_cnt += 1

if treffer_cnt < 3:
    print("Du hattest keinen Erfolg.")
else:
    print(f"Glückwunsch! Du hattest einen {treffer_cnt}er.")

# Aufgabe 13: Erweitere den Lottocode so, dass du in einem Loop
#             eine große Anzahl von Ziehungen machst. Zähle dabei 
#             deine Erfolge (3er, 4er, 5er, 6er).

print("\nAufgabe 13\n")

# Zähler für die Gewinner

cnt3er = 0
cnt4er = 0
cnt5er = 0
cnt6er = 0

for ziehungen in range(5_000_000):  # 1_000_000 Ziehungen, wir wollen mal nicht übertreiben ;)
    treffer_cnt = 0                 # Treffercounter wird bei jedem Loop zurückgesetzt.
    ziehung = random.sample(lostrommel, 6)  # Zufalls- Sample aus 1 - 49
    for lottozahl in ziehung:       # Vergleich mit Tippschein
        if lottozahl in tippschein:
            treffer_cnt += 1
    match treffer_cnt:              # Zuordnung zu den jeweiligen Gewinner- Zählern
        case 3:
            cnt3er += 1
        case 4:
            cnt4er += 1
        case 5:
            cnt5er += 1
        case 6:
            cnt6er += 1

print(f"Du hattest {cnt3er} Dreier.\nDu hattest {cnt4er} Vierer.\nDu hattest {cnt5er} Fünfer.\nDu hattest {cnt6er} Sechser.\n")

# Aufgabe 14: Generiere die folgende verschachtelte Liste mittels List Comprehension.
#             [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

# Herleitung über Loops

matrix3d_loop=[]
for k in range(3):
    liste_j=[]
    for j in range(3):
        liste_i=[]
        for i in range(3):
            liste_i.append(i+1+j*3+k*9)
        liste_j.append(liste_i)
    matrix3d_loop.append(liste_j)

#print(matrix3d_loop)

matrix3d=[[[i+1+j*3+k*9 for i in range(3)] for j in range(3)] for k in range(3)]
print(matrix3d)

# Aufgabe 15: Schreibe eine Funktion, die die Liste matrix3d zurückgibt, 
#             wobei die Längen der Listen über die Argumente parametrierbar sind.


def matrix3d(irange:int, jrange:int, krange:int)->list:
    """
    Bildet eine 3-fach verschachtelte Liste.
    """
    return [[[i+1+j*irange+k*irange*jrange for i in range(irange)] for j in range(jrange)] for k in range(krange)]

matrix3d_func = matrix3d(2,3,4)

print(matrix3d_func)


