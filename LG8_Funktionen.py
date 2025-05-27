# FUNKTIONEN
# DRY- Prinzip: Don't repeat yourself

def eine_funktion(name:str="Teilnehmer"):
    """
    Soll Hallo zu dem Namen sagen.\n
    @param1: Typ String - ein Name\n
    @return: None
    """
    return f"Hello {name}"
    print("Wird nicht ausgeführt")

hallo = eine_funktion()
print(hallo)
print(eine_funktion("Stefan"))

# Aufgabe 1: Schreibe eine Funktion, die einen String
#            für einen Namen als Argument übernimmt und 
#            eine Ausgabe erzeugt 'Hallo' + Name.

print("\nAufgabe 1\n")

def sayHello(name:str):
    if type(name)==str:
        return f"Hello {name}"
    else:
        return "Hello"
print()
print(sayHello(42))       # Hello
print(sayHello("Stefan"))  # Hello Stefan

# Aufgabe 2: Schreibe eine Funktion, die eine außerhalb der 
#            Funktion definierte Liste von Zahlen als Argument
#            übernimmt und ein zweites Zahlen- Argument, um das
#            die einzelnen Elemente erhöht werden.

print("\nAufgabe 2\n")

def addValue(seq:list, val:int|float):
    if (type(seq)==list) and (type(val)==int or type(val)==float):
        for idx in range(len(seq)):
            seq[idx]+=val
        # for num in seq:
        #     num += val
    if (type(seq)!=list): 
        print("Keine Liste übergeben.")
    if (type(val)!=int and type(val)!=float):
        print("Falscher Datentyp für Summand.")

liste = [0,1,2]

addValue(liste, 5)
print(liste)

# liste1 = ["0","1","2"]
# addValue(liste1, 5)       # Fehler!
addValue("liste", "5") # Fehlerausgaben für beide Params


# Aufgabe 3: Schreibe eine Funktion, die mehrere Münzwurfe
#            simuliert und die Häufigkeit von Kopf und Zahl
#            ausgibt. Nutze dazu eine geeignete Methode des 
#            random- Moduls.

print("\nAufgabe 3\n")

def multi_flipCoin(num):
    if type(num)==int:
        import random
        cntHead = 0
        cntTail = 0
        for _ in range(num):        
            if random.choice(["Kopf", "Zahl"]) == "Kopf":
                cntHead += 1
            else: cntTail += 1
        print(f"Es fielen {cntHead} x Kopf und {cntTail} x Zahl")
    else: print("Falsches Argument für Anzahl der Würfe.")

multi_flipCoin(30)
multi_flipCoin("30") # Fehlermeldung aus dem Else- Block.

# Aufgabe 4: Schreibe eine Funktion, 
#            die den größten Teiler einer Zahl findet.

print("\nAufgabe 4\n")

def maxDivisor(num):
    # div = num//2      # besser in Zeile 87
    if type(num) == int:
        if str(num) in "1,2,3":
            return f"{num} ist eine Primzahl"
        else:
            div = num//2
            while num % div != 0:
                div -= 1
            if div > 1:
                return f"Größter Teiler der Zahl {num} ist {div}."
            else:
                return f"{num} ist eine Primzahl"
    else: return "Keine Ganzzahl übergeben."

print(maxDivisor(120001501))
# print(maxDivisor(45))
# print(maxDivisor("45"))

def maxDivisor1(num:int)->int:
    div = num//2
    while num % div != 0:
        div -= 1
    return div

# Variante Alireza
def größteteiler(zahl:int)->int:
    for digit in range(zahl//2,0,-1):
        if zahl%digit==0:
            #print(digit)
            #break
            return digit

import time

# Zeitmessung beider Varianten
t1=time.time()
print(maxDivisor1(120001501))
t2=time.time()
print(größteteiler(120001501))
t3=time.time()

print(f"Stefan: {t2-t1}, Alireza: {t3-t2}")

# Aufgabe 5: Schreibe eine Funktion zur Kreisberechnung, die zwei Argumente übernimmt: einen Zahlenwert
# und einen String, der aussagt, ob dieser Zahlenwert als Radius, Umfang oder Fläche zu verstehen ist.
# Radius soll dabei als Defaultwert eingestellt sein. Die Funktion soll dann die jeweils restlichen 
# Werte ausgeben. Du wirst das Modul 'math' einbinden müssen.

print("\nAufgabe 5\n")

# Alternative 1
def kreis(val:int|float, mod:str="r")->None:    # Argument "mod" ist per default mit "r" für Radius belegt
    '''
    mod bezeichnet, welchen Wert die übergebene 
    Variable darstellt
    Radius="r"      Durchmesser="d"
    Fläche="a"      Umfang="u"
    '''
    from math import pi, sqrt   # Import der Mathebibliothek für PI und Wurzelziehen

    match mod:  # die verschiedenen Berechnungen in Abhängigkeit vom Modus
        case "r":
            d=2*val
            a=pi*val**2
            u=pi*2*val
            print(f"Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "d":
            r=val/2
            a=(pi*val**2)/4
            u=pi*val
            print(f"Radius: {round(r, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "a":
            r=sqrt(val/pi)
            d=2*r
            u=pi*2*r
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Umfang: {round(u, 2)}")
        case "u":
            r=val/(2*pi)
            d=2*r
            a=pi*r**2
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}")

kreis(10)       # Aufruf der Funktion mit nur einem Argument (default=Radius)
kreis(20, "a")  # Aufruf mit zwei Argumenten, erster Wert gilt als Fläche

# Alternative 2 (sparsamer)
def kreis1(val:int|float, mod:str="r")->None:    # Argument "mod" ist per default mit "r" für Radius belegt
    '''
    mod bezeichnet, welchen Wert die übergebene 
    Variable darstellt
    Radius="r"      Durchmesser="d"
    Fläche="a"      Umfang="u"
    '''
    from math import pi, sqrt   # Import der Mathebibliothek für PI und Wurzelziehen

    radius = 0

    match mod:  # die verschiedenen Berechnungen in Abhängigkeit vom Modus
        case "r":
            radius = val
        case "d":
            radius = val/2
        case "a":
            radius = sqrt(val/pi)
        case "u":
            radius = val/(2*pi)

    d=2*radius
    a=pi*radius**2
    u=pi*2*radius
    print(f"Radius: {round(radius, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")

kreis1(10)       # Aufruf der Funktion mit nur einem Argument (default=Radius)
kreis1(20, "a")  # Aufruf mit zwei Argumenten, erster Wert gilt als Fläche


# Aufgabe 6: Schreibe eine Funktion, die zwei Koordinaten (Punkte auf einer Geraden)
#            als Argumente übernimmt und den Y- Achsenabschnitt der Geraden
#            zurückgibt. 
#            Zur Prüfung deines Ergebnisses:
#            https://www.mathepower.com/lineare_funktionen.php

print("\nAufgabe 6\n")

def linearFunktion(p1:list|tuple, p2:list|tuple):
    # m = (y2 - y1)/(x2 - x1)
    m = (p2[1] - p1[1] / p2[0] - p1[0])
    # Grundformel nach n umstellen
    # n = f(x) - mx
    n = p1[1] - m*p1[0]
    print(f"Die Formel der Geraden ist f(x) = {m}x + {n}. Die Y- Achse wird bei y = {n} geschnitten.")
    print(f"Die Formel der Geraden ist f(x) = {m}x {"+" if n>=0 else "-"} {abs(n)}. Die Y- Achse wird bei y = {n} geschnitten.")

linearFunktion((5,7), (-2,3))

# Aufgabe 7: Schreibe einen einfachen Passwortgenerator, der als Argument
#            die Länge des Passworts übernimmt und ein entsprechendes 
#            Passwort bestehend aus Groß- und Kleinbuchstaben, sowie Zahlen
#            und Sonderzeichen. Sieh dir dazu das Modul 'string' an:
#            https://www.geeksforgeeks.org/python-string-module/
#            Für die Fortgeschrittenen:
#            Übergebe einen String als zweites Argument, der 
#            Ausschlusszeichen enthält, die man im Passwort nicht haben will.
#            Sieh dir dazu den Datentyp 'set' an.

print("\nAufgabe 7\n")

def pwgenSimple(pwLength:int, ausschluss:str="")->str:
    """
    @param pwLength: Integerzahl für die Anzahl der auszugebenen Zeichen
    @return: Zufällige Zeichenkette
    """
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    from random import sample 
    pwPool=list(set(ascii_lowercase + ascii_uppercase + digits + punctuation) - set(ausschluss))
    print(sorted(pwPool))     # nur einkommentieren, um den Zeichenpool zu sehen
    return "".join(sample(pwPool, pwLength))    # Sampleliste wird in einen leeren String gejoint

#print(pwgenSimple(20))
print(pwgenSimple(20, ";.@A12"))


# Aufgabe 8: Erweitere deinen Passwortgenerator so, dass du die Anzahl
#            der jeweiligen Zeichen bestimmen kannst.

print("\nAufgabe 8\n")

def pwgenPro(lows:int, caps:int, nums:int, specs:int=0, ausschluss:str="")->str:
    from random import sample, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    lowLetters=sample(list(set(ascii_lowercase)-set(ausschluss)), lows)
    capLetters=sample(list(set(ascii_uppercase)-set(ausschluss)), caps)
    numbers=sample(list(set(digits)-set(ausschluss)), nums)
    specChar=sample(list(set(punctuation)-set(ausschluss)), specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    shuffle(pw)
    return "".join(pw)

print(pwgenPro(2,3,4,4,";.@a12"))