liste_1 = [1,2,3,4,5,6,7,8,9,10]
liste_2 = [11,12,13,14,15]
liste_3 = liste_2.copy()
liste_3[0] = 20
#print(liste_2)
liste_5 = [2,5,4,1]
liste_5.sort(reverse=True)
print(liste_5)
#print(liste_5.sort())
# print(liste_5)
# print("".join(sorted("michael")))
#liste_5.reverse()
print(reversed(liste_5))
print(liste_5)


#liste_4 = ["16","17","16"]
#liste_1.append("Michael")
#liste_1.extend("Michael")
#liste_1 += liste_2 
#liste_1.insert(5,liste_2)
#print(":".join(liste_4))
#print(liste_4.index("16"))

#a = liste_4.pop(0)
#print(liste_4.pop(0))
# while "16" in liste_4:
#     liste_4.remove("16")

# for zahl in liste_4:
#     if zahl == "16":
#         liste_4.remove("16")
# print(liste_4)

# LOOPS

liste_1 = [1,2,3,4,5,6,7,8,9,10]

# for zahl in liste_1:
#     print(zahl, end=" ")

# print()

for zahl in range(0,10, 2):
    print(liste_1[zahl], end=" ")

print()

for zahl in range(0,len(liste_1)//2):
    print(liste_1[zahl], end=" ")

# range(start, stop, step) # wenn alle 3 Argumente übergeben werden
# range(10)

for zahl in (list(range(10))+list(range(11, 21))):
    print(zahl, end=" ")

liste_2 = (list(range(10))+list(range(11, 21)))

for zahl in liste_2:
    print(zahl, end=" ")

print(zahl)

cnt = 0
while cnt < 5:
    print(cnt)
    cnt+=1

cnt = 0
while True:
    if cnt == 5:
        break
    print(cnt)
    cnt+=1

# Funktioniert nicht!
# cnt = 0
# while condition := True:
#     if cnt == 5:
#         condition = False 
#     print(cnt)
#     cnt+=1

for zahl in range(10):
    if zahl <= 5:
        continue
    print(zahl)

print()

for zahl in range(10):
    if zahl == 5:
        break
    print(zahl)


