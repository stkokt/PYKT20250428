# Aufgabe 1: Die folgende Liste enthält 80 Elemente. Nutze List- Slicing, um 
#            a) die erste Hälfte auszugeben.
#            b) die letzten 15 Elemente auszugeben.
#            c) die mittleren 40 Elemente auszugeben.
#            d) die letzte Hälfte rückwärts auszugeben. 

big_list =[41, 19, 21, 7, 18, 26, 25, 28, 24, 14, 
           17, 35, 18, 11, 19, 20, 44, 33, 7, 33, 
           7, 35, 5, 35, 46, 50, 9, 4, 41, 39,
           42, 39, 15, 35, 45, 44, 30, 49, 37, 25,
           2, 41, 1, 5, 12, 39, 23, 20, 28, 21,
           17, 39, 36, 18, 22, 49, 36, 4, 42, 16,
           35, 19, 47, 27, 23, 40, 9, 38, 49, 26,
           4, 29, 10, 43, 15, 12, 45, 47, 25, 34]

print("\nAufgabe 1a\n")
print(big_list[:40])  # oder big_list[:len(big_list)//2]

print("\nAufgabe 1b\n")
print(big_list[65:]) # oder big_list[len(big_list)-15:]

print("\nAufgabe 1c\n")
print(big_list[20:60]) # oder big_list[20:len(big_list)-20]

# Alternative Ruth
auswahl = big_list [len(big_list)//2 - len(big_list)//4 : \
                    len(big_list)//2 + len(big_list)//4]
print(auswahl)

print("\nAufgabe 1d\n")
print(big_list[80:39:-1]) # oder big_list[len(big_list):len(big_list)//2-1:-1]

print("\nAufgabe 1d Alireza\n")
# liste_a=big_list[(-1)*int(len(big_list)/2)::-1]
# print(liste_a)

# Aufgabe 2: Slice und konkatiniere die folgende Liste so,
#            dass sie sortiert ist und gebe sie aus.

liste = [5,4,3,2,1,10,9,8,7,6]

print("\nAufgabe 2\n")

liste_sorted = liste[4::-1] + liste[9:4:-1]
print(liste_sorted)

# print(sorted(liste))
# liste.sort()

# Aufgabe 3: Gebe die Quartalsumsätze via List- Slicing aus.
#    	     Wer sich zutraut, benutzt dazu einen Loop.

print("\nAufgabe 3\n")

monatsumsatz = [1,2,3,4,5,6,7,8,9,10,11,12]

Q1 = sum(monatsumsatz[0:3])
Q2 = sum(monatsumsatz[3:6])
Q3 = sum(monatsumsatz[6:9])
Q4 = sum(monatsumsatz[9:])

# print(f"Quartalsumsätze {Q1}, {Q2}, {Q3}, {Q4}")
 
s=0
e=3
for q in range(s,e+1):
    print(f"Q{q+1}:",sum(monatsumsatz[s:e]))
    s+=3
    e+=3

# Aufgabe 4:

liste1 = [1,2,3,5,6,7,5,12,50,4,5,60]

# Aufgabe 4a: Slice die Liste1 in einem Loop durch Verschieben
#             des Start- Parameters so, dass die Summe der restlichen
#             Liste kleiner 100 ist. Der Loop soll dann abgebrochen und die 
#             gekürzte Liste ausgegeben werden.

# >            (<100)             <
#  |x ->| | | | | | | | | | |stop|

print("\nAufgabe 4a\n")
#              0,1,2,3,...,11
for x in range(len(liste1)):
    if sum(liste1[x:])<100:
        print(liste1[x:])
        break


# Aufgabe 4b: Slice die Liste1 in einem Loop durch Verschieben
#             des Stop- Parameters so, dass die Summe der restlichen
#             Liste den Wert 100 gerade überschritten hat. 
#             Der Loop soll dann abgebrochen und die gekürzte 
#             Liste ausgegeben werden.

# >            (>100)            <
#  |start| | | | | | | | | | |<-x|

print("\nAufgabe 4b\n")
#                   11,10,9,...,2,1
for x in reversed(range(len(liste1))):
    if sum(liste1[:x])<100:
        print(liste1[:x+1])
        break

for index, zahl in enumerate(liste1):
    start = 0 # bleibt gleich. Hätte es auch weglassen können und nur ":"" schreiben
    stop = len(liste1) - index 
    #print(index)
    gekuerzte_liste = liste1[start:stop-1]
    summe = sum(gekuerzte_liste) # alternativ ginge hier auch: summe += liste1[index], wenn über dem Loop: summe=liste1[0]
    #print(gekuerzte_liste)
    #print(f"Summe: {summe}")
    if summe >= 100:
        print (f"Summe des Anfangs der Liste ist größer als 100 bei Zahl: {liste1[stop-1]} auf Index: {stop-1}")
        print(f"Gekürzte Liste: {gekuerzte_liste}")
        break

# Aufgabe 4c: Slice die Liste1 in einem Loop durch Verschieben
#             der Start- und Stop- Parameter so, dass die Summe der restlichen
#             Liste kleiner 100 ist. Der Loop soll dann abgebrochen und die 
#             gekürzte Liste ausgegeben werden.

# >            (<100)           <
#  |x->| | | | | | | | | | |<-x|

print("\nAufgabe 4c\n")
# liste1 = [1,2,3,5,6,7,5,12,50,4,5,60]
# 0,1,2,3,4,5,6,7,8,9,10,11
for x in range(len(liste1)):
    if sum(liste1[x:len(liste1)-x])<100:
        print(liste1[x:len(liste1)-x])
        break

print("\nIris\n")

for idx, n in enumerate(liste1):       # start, stop, step 
    print(liste1[idx:len(liste1)-idx])
    summe_liste = sum(liste1[idx:len(liste1)-idx])
    print(f"liste2: {summe_liste}")     
    if summe_liste  < 100 :
         break
    
print(f"liste2_fin: {summe_liste}")