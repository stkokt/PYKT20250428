# pass - um Funktionsdefinitionen zunächst offen zu lassen.

def anyFunction():
    pass

# Ende pass


# Verschachtelte Funktionen

def outerFunc(name):
    def innerFunc():
        return name
    print("Hallo", innerFunc())

outerFunc("Stefan")

# Ende Verschachtelte Funktionen


# Namensräume

x = 5   # globale Variable (global)

def scope():
    x = 10
    def glob():
        global x
        x+=1
        print("Aus glob(): ",x)
    def nonloc():
        nonlocal x  # nonlokale Variable aus Zeile 26
        x+=1
        print("Aus noneloc(): ",x)
    def loc():
        x=15
        print("Aus loc(): ",x)
    glob()      # -> 5
    nonloc()    # -> 10
    loc()       # -> 15

scope()

# Ende Namensräume


# Args und Kwargs (Argumente und Keyword- Argumente)
# um mehrere Argumente zu übernehmen

# *args
def sum(*args):
    a = args[0]
    for num in range(1, len(args)):
        a+=args[num]
    return a

print(sum(2,3,8,9))

# kwargs (Keywordarguments)

def quark(**kwargs):
    print(type(kwargs))
    print(kwargs)

quark(kw1 = "Hallo", kw2 = "Stefan")


def varArgsKwargs(var, *args, **kwargs):
    '''
    Es muss nicht *args und **kwargs heißen, 
    wichtig sind die Sternchen.
    *args wird als Tupel interpretiert,
    **kwargs als Dictionary.
    '''
    print(f"Das ist die Variable: {var}.")
    print(f"Das ist das Args- Tupel: {args}")
    print(f"Das ist das Kwargs- Dictionary: {kwargs}")
    for value in kwargs.values():
        print(args[0]*value)

varArgsKwargs("Var", 5,"m",3.14, kwargs1 = "Hallo", kwargs2 = "Welt")

# Beispiel
namen = {
    "Anna Müller": "w",
    "Laura Schmidt": "w",
    "Max Mustermann": "m",
    "Maria Becker": "w",
    "Sophie Wagner": "w",
    "Paul Meier": "m",
    "Lukas Schneider": "m",
    "Julia Fischer": "w",
    "Felix Weber": "m",
    "Jonas Hoffmann": "m"
}


def hallo(namedict:dict, *geschlecht, **anrede):
    for name, sex in namedict.items():
        if sex == geschlecht[0]:  # Index 0 der Tupels geschlecht
            print(f"Hallo {list(anrede.values())[0]} {name.split()[-1]}!")
        if sex == geschlecht[1]:  # Index 1 der Tupels geschlecht
            print(f"Hallo {list(anrede.values())[1]} {name.split()[-1]}!")
    # die Values des Dictionarys am Index 1 gesplittet und davon das letzte Element
# Aufruf:
hallo(namen,'m','w',geschlecht1="Herr", geschlecht2="Frau")

# Ende Args und Kwargs


# Lambda- Funktionen
# sind kurze, "anonyme" Funktionen
# Sie können an Ort und Stelle geschrieben und ausgeführt werden.

# kurze Funktion
def multi(a,b):
    return a*b
print(multi(10,5))

# kürzer
multi1 = lambda a,b: a*b
print(multi1(10,5))

# noch kürzer
print((lambda a,b: a*b)(5,10))

# Ende Lambda


# Die Builtin- Funktionen filter() und map()

daten = [0,1,0,5,0,60,74,32,5,6,-4,3,6,8,52,-12,1000]

# filter
# filtert die Daten aus einer Datenreihe gemäß einer Funktion
daten1 = list(filter(lambda x: x>0 and x<100, daten))
print(daten1)

# map
# map wendet eine Funktion auf eine Datenreihe an
daten2 = list(map(lambda x: x>0 and x<100, daten))
# True, wenn 'daten' zwischen 0 und 100, sonst False
print(daten2)