# 2_Strings und IfElse

"""
Die Methoden der String- Klasse:

1. str.capitalize(): Konvertiert den ersten Buchstaben des Strings in einen Großbuchstaben und alle anderen in Kleinbuchstaben.

2. str.casefold(): Wie `lower()`, aber aggressiver, da es für caseless matches verwendet wird.

3. str.center(width[, fillchar]): Zentriert den String in einem Feld der angegebenen Breite, füllt die Ränder mit dem angegebenen Füllzeichen (Standard ist Leerzeichen).

4. str.count(sub[, start[, end]]): Zählt die nicht überlappenden Vorkommen der Unterzeichenkette im Bereich [start, end].

5. str.encode(encoding="utf-8", errors="strict"): Kodiert den String mit dem angegebenen Kodierungsverfahren.

6. str.endswith(suffix[, start[, end]]): Gibt `True` zurück, wenn der String mit dem angegebenen Suffix endet.

7. str.expandtabs(tabsize=8): Ersetzt Tabulatoren im String durch Leerzeichen.

8. str.find(sub[, start[, end]]): Gibt den niedrigsten Index im String zurück, an dem die Unterzeichenkette gefunden wird.

9. str.format(*args, **kwargs): Formatiert den String mit den angegebenen Argumenten.

10. str.format_map(mapping): Ähnlich wie `format()`, aber verwendet ein Mapping-Objekt für die Argumente.

11. str.index(sub[, start[, end]]): Wie `find()`, wirft aber einen Fehler, wenn die Unterzeichenkette nicht gefunden wird.

12. str.isalnum(): Gibt `True` zurück, wenn alle Zeichen im String alphanumerisch sind.

13. str.isalpha(): Gibt `True` zurück, wenn alle Zeichen im String alphabetisch sind.

14. str.isascii(): Gibt `True` zurück, wenn der String nur ASCII-Zeichen enthält.

15. str.isdecimal(): Gibt `True` zurück, wenn alle Zeichen im String Dezimalzahlen sind.

16. str.isdigit(): Gibt `True` zurück, wenn alle Zeichen im String Ziffern sind.

17. str.isidentifier(): Gibt `True` zurück, wenn der String ein gültiger Bezeichner ist.

18. str.islower(): Gibt `True` zurück, wenn alle Buchstaben im String Kleinbuchstaben sind.

19. str.isnumeric(): Gibt `True` zurück, wenn alle Zeichen im String numerisch sind.

20. str.isprintable(): Gibt `True` zurück, wenn alle Zeichen im String druckbar sind.

21. str.isspace(): Gibt `True` zurück, wenn alle Zeichen im String Leerzeichen sind.

22. str.istitle(): Gibt `True` zurück, wenn der String im Titel-Format ist.

23. str.isupper(): Gibt `True` zurück, wenn alle Buchstaben im String Großbuchstaben sind.

24. str.join(iterable): Verbindet die Elemente eines iterierbaren Objekts zu einem String.

25. str.ljust(width[, fillchar]): Füllt den String links mit dem angegebenen Füllzeichen auf die angegebene Breite auf.

26. str.lower(): Konvertiert alle Buchstaben im String in Kleinbuchstaben.

27. str.lstrip([chars]): Entfernt führende Leerzeichen (oder angegebene Zeichen) vom String.

28. str.maketrans(x[, y[, z]]): Gibt eine Übersetzungstabelle zurück, die von `translate()` verwendet werden kann.

29. str.partition(sep): Teilt den String am ersten Vorkommen des Trennzeichens und gibt ein 3-Tupel zurück.

30. str.replace(old, new[, count]): Ersetzt Vorkommen der alten Unterzeichenkette durch die neue Unterzeichenkette.

31. str.rfind(sub[, start[, end]]): Gibt den höchsten Index im String zurück, an dem die Unterzeichenkette gefunden wird.

32. str.rindex(sub[, start[, end]]): Wie `rfind()`, wirft aber einen Fehler, wenn die Unterzeichenkette nicht gefunden wird.

33. str.rjust(width[, fillchar]): Füllt den String rechts mit dem angegebenen Füllzeichen auf die angegebene Breite auf.

34. str.rpartition(sep): Teilt den String am letzten Vorkommen des Trennzeichens und gibt ein 3-Tupel zurück.

35. str.rsplit(sep=None, maxsplit=-1): Teilt den String von rechts nach links.

36. str.rstrip([chars]): Entfernt nachfolgende Leerzeichen (oder angegebene Zeichen) vom String.

37. str.split(sep=None, maxsplit=-1): Teilt den String in eine Liste von Unterzeichenketten.

38. str.splitlines([keepends]): Teilt den String an Zeilenumbrüchen und gibt eine Liste von Zeilen zurück.

39. str.startswith(prefix[, start[, end]]): Gibt `True` zurück, wenn der String mit dem angegebenen Präfix beginnt.

40. str.strip([chars]): Entfernt führende und nachfolgende Leerzeichen (oder angegebene Zeichen) vom String.

41. str.swapcase(): Konvertiert Großbuchstaben in Kleinbuchstaben und umgekehrt.

42. str.title(): Konvertiert den ersten Buchstaben jedes Wortes in einen Großbuchstaben.

43. str.translate(table): Ersetzt Zeichen im String basierend auf der Übersetzungstabelle.

44. str.upper(): Konvertiert alle Buchstaben im String in Großbuchstaben.

45. str.zfill(width): Füllt den String mit führenden Nullen auf die angegebene Breite auf.
"""

# Aufgabe 1: Prüfe, ob eine String- Variable Text enthält
#            oder leer ist. Gebe eine entsprechende Rückmeldung aus.

print("\nAufgabe 1\n")

text1 = "\t"
text2 = "Hallo"

# Variante 1
if text1.isspace(): # Prüfung auf Whitespaces (auch Leerzeichen oder TAB)
    print("String enthält keine Zeichen.")
else:
    print("String enthält Zeichen.")

# Variante 2
if text1:   # Prüfung, ob Länge > 0. Besser: if len(text1)>0
    print("String enthält Zeichen")
else:
    print("String enthält keine Zeichen")
    

# Aufgabe 2: Prüfe eine String- Variable. Enthält sie
#            nur Kleinbuchstaben, soll der String umgewandelt 
#            werden, sodass jedes Wort mit einem Großbuchstaben
#            beginnt.

print("\nAufgabe 2\n")

text3 = "Lorem ipsum dolor sit amet"
text4 = "2sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat"

if text3.islower():
    text3 = text3.title()

print(text3)

if text4.islower():
    text4 = text4.title()

print(text4)

# Aufgabe 3: Prüfe eine Anrede darauf, ob sie mit "Frau" oder "Herr"
#            beginnt.

print("\nAufgabe 3\n")

anrede1 = "Frau Müller"
anrede2 = "Herr Schmidt"
#print(anrede1.find("Frau")>=0)
print("Frau" in anrede1.split())

if anrede1.startswith("Frau"):
    print(f"{anrede1} ist weiblich.")
else:
    print(f"{anrede1} ist männlich.")

if anrede2.startswith("Frau"):
    print(f"{anrede2} ist weiblich.")
else:
    print(f"{anrede2} ist männlich.")

# Aufgabe 4: Gebe einen vollständigen Namen ein (Vor- und Zuname) und
#            prüfe, ob er mit 'Schmidt' endet.

print("\nAufgabe 4\n")

name = input("Gebe deinen vollständigen Namen ein:\n")

if name.endswith("Schmidt"):
    print("Du bist ein Schmidt!")
else:
    print("Du bist kein Schmidt!")

# Aufgabe 5: Prüfe folgenden String, ob er das Wort 'amet' enthält.

print("\nAufgabe 5\n")

lorem = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam."

# Variante 1:
if lorem.find("amet"):  # Besser: lorem.find("amet") >= 0
    print("String enthält das Wort 'amet'.")
else:
    print("String enthält das Wort 'amet' nicht.")

# Aufgabe 6: Prüfe einen String darauf, ob er die Struktur einer 
#            Email- Adresse darstellt. 
#            Mindestbedingung: Ein '@' muss enthalten sein.
#            Weiterführend: Enthält einen Punkt nach dem '@'.

print("\nAufgabe 6\n")

mail = "stefan.koschnik@mein-karrieretutor.de"

# Mindestbedingung:

if '@' in mail:
    print("Gültige Mailadresse.")
else:
    print("Keine gültige Mailadresse.")

# Weiterführend:

mail_suffix = mail.split("@")[1]
print(mail_suffix)

if '@' in mail and mail_suffix.count(".") == 1:
    print("Gültige Mailadresse.")
else:
    print("Keine gültige Mailadresse.")

# Aufgabe 7: Simuliere eine PIN- Eingabe (4- stellig). Prüfe, 
#            ob die Eingabe nur aus Ziffern besteht.

print("\nAufgabe 7\n")

pin = input("Gebe deine PIN ein:\n")

if pin.isdigit() and len(pin) == 4:
    print("PIN- Format ist gültig.")
else:
    print("Ungültiges PIN- Format!")

# Aufgabe 8: Bestimme die Anzahl der Sätze in folgendem String.

print("\nAufgabe 8\n")

lorem2 = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
        sed diam nonumy eirmod tempor invidunt ut labore et dolore 
        magna aliquyam erat, sed diam voluptua. At vero eos et accusam 
        et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
        no sea takimata sanctus est Lorem ipsum dolor sit amet."""

print(f"Der String 'lorem2' besteht aus {lorem2.count(".")} Sätzen.")

# Aufgabe 9: Entferne die Sternchen aus folgendem String.

print("\nAufgabe 9\n")

sternchen = "**Lorem ipsum* dolor**"

print(sternchen.replace("*",""))
print(sternchen.strip("*"))

# Aufgabe 10: Löse die Rindvieh- Aufgabe.
