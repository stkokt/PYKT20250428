### Arbeitsblatt: Python-Aufgaben mit `int`, `float` und `string` Variablen

#### Aufgaben

# 1. Addiere zwei `int`-Werte und gebe das Ergebnis aus:
print("\nAufgabe 1\n")

a = 5
b = 10
result = a + b
print(result)
print(5+10)


# 2. Subtrahiere zwei `float`-Werte und gebe das Ergebnis aus:
print("\nAufgabe 2\n")

x = 7.5
y = 3.2
result = x - y
print(result)


# 3. Multipliziere einen `int` und einen `float`-Wert und gebe das Ergebnis aus:
print("\nAufgabe 3\n")

a = 4
b = 2.5
result = a * b
print(result)


# 4. Dividiere zwei `int`-Werte und gebe das Ergebnis aus:
print("\nAufgabe 4\n")

a = 10
b = 2
result = a / b 
print(result)
print(type(result))  # Das Ergebnis der Division ist vom Typ 'float'.


# 5. Mache eine ganzzahlige Division von zwei `int`-Werte und gebe das Ergebnis aus:
print("\nAufgabe 5\n")

a = 10
b = 3
result = a // b     # Operator für ganzzahlige Division.
result = int(a / b) # Alternativ: Dividieren und anschließend in einen Integer umwandeln.
print(result)

print(int(1.9999_9999_9999_9999))   # Wird zu 2 bei 16 Nachkommastellen auf 9.

# 6. Ermittle den Rest einer Division (Modulo) von zwei `int`-Werten:
print("\nAufgabe 6\n")

a = 10
b = 3
result = a % b  # z.B. 10 % 3 = 1 oder 12 % 5 = 2
print(result)


# 7. Potenziere einen `int` mit einem `float`:
print("\nAufgabe 7\n")

a = 2
b = 3.0
result = a ** b     # Quadrieren eines Wertes: a*a oder a**2 
print(result)


# 8. Verbinde zwei `string`-Werte (Konkatenation):
print("\nAufgabe 8\n")

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)
print(str1,str2)

# 9. Wiederhole einen `string`-Werte xmal (nicht händisch sondern per Operator):
print("\nAufgabe 9\n")

str1 = "Python"
result = str1*3     # Strings lassen sich auch multiplizieren und addieren.
print(result)


# 10. Gebe nur das erste Zeichen einer `string`- Variablen aus:
print("\nAufgabe 10\n")

str1 = "Python"
result = str1
print(str1[0])      # Index- basierter Zugriff, beginnt immer bei 0.


# 11. Ermittle die Länge eines `string`-Wertes:
print("\nAufgabe 11\n")

str1 = "Python"
result = len(str1)  # len() = Python Builtin- Funktion
print(result)


# 12. Konvertiere einen `int` zu einem `float`:
print("\nAufgabe 12\n")

a = 5
result = float(a) # float() = Python Builtin- Funktion
print(result)


# 13. Konvertiere einen `float` zu einem `int`:
print("\nAufgabe 13\n")

x = 7.5
result = int(x) # int() = Python Builtin- Funktion
print(result)


# 14. Konvertiere einen `int` zu einem `string':
print("\nAufgabe 14\n")

a = 42
result = str(a) # str() = Python Builtin- Funktion
print(result)


# 15. Konvertiere einen `float` zu einen `string`:
print("\nAufgabe 15\n")

x = 3.14
result = str(x)
print(result)


# 16. Konvertiere einen `string` zu einem `int`:
print("\nAufgabe 16\n")

str1 = "123"
result = int(str1)
print(result)


# 17. Konvertiere einen `string` zu einem `float`:
print("\nAufgabe 17\n")

str1 = "3.14"
result = float(str1)
print(result)

# 18. Formatiere einen `string` mit Platzhaltern für einen `int` und einen `float`- Wert:
print("\nAufgabe 18\n")

a = 5
b = 3.14
result = f"a = {a}, b = {b}"    # Formatierter String (f- String)
result1 = "a = {}, b = {}".format(a,b)
print(result)
print(result1)


# 19. Gebe den Absolutwert eines negativen `int`-Wertes aus:
print("\nAufgabe 19\n")

a = -5
result = abs(a) # abs() = Python Builtin- Funktion
print(result)


# 20. Runde einen `float`-Wert auf zwei Nachkommastellen:
print("\nAufgabe 20\n")

x = 35.14159
#result = round(x, 1)   # round() = Python Builtin- Funktion
#print(result)
result = round(x,-1)
print(result)


# 21. **Bitweise Operatoren** Ver-UND-e zwei `int`-Werte:
print("\nAufgabe 21\n")

a = 5  # 0101 in binär
b = 3  # 0011 in binär
result = a & b
print(result)

# 0101 &        # Ergebnis wird 1, wenn beide Bits auf 1 stehen.
# 0011 
# ______
# 0001

# 22. **Bitweise Operatoren** Ver-ODER-e zwei `int`-Werte:
print("\nAufgabe 22\n")

a = 5  # 0101 in binär
b = 3  # 0011 in binär
result = a | b
print(result)

# 0101 |         # Ergebnis wird 1, wenn eines der Bits auf 1 steht.
# 0011 
# ______
# 0111 -> 4+2+1 = 7

print(bin(7))   # bin() = Python Builtin- Funktion, zeigt die Binärreihe

# 23. **Bitweise Operatoren** Ver-XODER-e zwei `int`-Werte:
print("\nAufgabe 23\n")

a = 5  # 0101 in binär
b = 3  # 0011 in binär
result = a ^ b
print(result)

# 0101 ^        # Ergebnis wird 1, wenn nur(!) eines der Bits auf 1 steht.
# 0011 
# ______
# 0110


# 24. **Bitweise Operatoren** Ver-NOT-e einen `int`-Werte:
print("\nAufgabe 24\n")

a = -5  
result = ~a
print(result)

# Faustregel für NOT in Python:
# Addiert 1 und dreht das Vorzeichen
# Also: NOT 5 = -6 oder NOT -10 = 9 

# 25. **Bitweise Operatoren** Shifte einen `int`-Wert zunächst nach links und dann wieder nach rechts:
print("\nAufgabe 25\n")

a = 5  # 0101 in binär
result = a << 2 
print(result)   
# 0101 -> 1010 = 10

b = 5
result = b >> 1
print(result)
# 0101 -> 0010 = 2

# Shift- Operatoren verschieben die Bitreihe zu einer Seite
# und füllen auf der anderen Seite mit 0 auf. Dadurch kann 
# es zu Informationsverlust kommen, wenn auf 1 gekippte Bits
# auf der rechten Seite "rausfallen".
