# PWGen mit Ausschlusszeichen

def pwgenSimple(pwLength:int, ausschluss:str="")->str:
    """
    @param pwLength: Integerzahl für die Anzahl der auszugebenen Zeichen
    @return: Zufällige Zeichenkette
    """
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    from random import sample 
    pwPool=list(set(ascii_lowercase + ascii_uppercase + digits + punctuation) - set(ausschluss))
    # print(sorted(pwPool))     # nur einkommentieren, um den Zeichenpool zu sehen
    return "".join(sample(pwPool, pwLength))    # Sampleliste wird in einen leeren String gejoint

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


if __name__ == "__main__":
    print(pwgenSimple(20, ";.@A12"))
    print(pwgenPro(2,3,4,4,";.@A12"))

