# Rindvieh

janein=input("Funktioniert die Anlage? j/n\n")

if janein=="j":
    print("Fummel bloß nicht dran rum")
    print("Alles klar!")
else:
    janein=input("Hast du dran rumgespielt? j/n\n")
    if janein=="j":
        print("Du Rindvieh!")
        janein=input("Hat es jemand gemerkt? j/n\n")
        if janein=="j":
            print("Du armes Schwein!")
            janein=input("Kannst du jemandem die Schuld zuschieben? j/n\n")
            if janein=="n":
                print("Du armes Schwein!")
            else:
                print("Alles klar!")
        else:
            print("Pfeiffe unauffällig 'La Paloma' und verschwinde!")
            print("Alles klar!")
    else:
        janein=input("Wird man dich verantwortlich machen? j/n\n")
        if janein=="j":
            print("Du armes Schwein!")
            janein=input("Kannst du jemandem die Schuld zuschieben? j/n\n")
            if janein=="n":
                print("Du armes Schwein!")
            else:
                print("Alles klar!")
        else:
            print("Kümmer dich nicht drum!")
            print("Alles klar!")
                            

