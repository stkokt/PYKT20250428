import PWGen
import tkinter as tk

# PyQt, pyside6, pygame, wxwidgets, kivy

def generate():
    lbl_Passwort.configure(text = PWGen.pwgenSimple(int(in_AnzahlZeichen.get()), in_NoChar.get()))
    #print(PWGen.pwgenSimple(int(in_AnzahlZeichen.get()), in_NoChar.get()))

def copyClipboard():
    lbl_Passwort.clipboard_clear()
    lbl_Passwort.clipboard_append(lbl_Passwort.cget('text'))

root = tk.Tk()

root.title("Passwortgenerator")
root.geometry('400x400')
root.resizable(False,False)

# Create Widgets

# Label für Eingabe Anzahl Zeichen
lbl_AnzahlZeichen = tk.Label(master = root, text = "Anzahl Zeichen", font=('Arial Black', 10), bg = 'RED')

# Eingabefeld Anzahl
in_AnzahlZeichen = tk.Entry(master = root)

# Label Ausschlusszeichen
lblNoChar = tk.Label(master=root, text='Auschlusszeichen', font=('Arial Black', 10),bg='RED')

# Eingabefeld Ausschlusszeichen
in_NoChar = tk.Entry(root)

# Button zum Generieren
btn_Gen = tk.Button(master = root, text="Generiere", font=('Arial Black', 10), command=generate)

# Button zum Kopieren in die Zwischenablage
btn_GenCopy = tk.Button(master=root, text='Kopiere in Zwischenablage', font=('Arial Black', 10), command = copyClipboard)

# Ausgabe des Passworts (Label)
lbl_Passwort = tk.Label(master=root, text='Passwort', font=('Arial Black', 20),bg='RED')

# Layout Widgets
# pack()

# lbl_AnzahlZeichen.pack(pady=10)
# in_AnzahlZeichen.pack()
# lblNoChar.pack(pady=10)
# in_NoChar.pack()

# grid()
# lbl_AnzahlZeichen.grid(row = 0, column=0, padx=10 , pady=10, sticky='w')
# in_AnzahlZeichen.grid(row = 0, column = 1, padx=10 , pady=10, sticky='w')
# lblNoChar.grid(row = 1, column = 0, padx=10 , pady=10, sticky='w')
# in_NoChar.grid(row = 1, column = 1, padx=10 , pady=10, sticky='w')

# place()
lbl_AnzahlZeichen.place(x=30, y=30)
in_AnzahlZeichen.place(x=200, y=30, width=150)
lblNoChar.place(x=30, y=80)
in_NoChar.place(x=200, y=80,width=150)
btn_Gen.place(x=30, y=130)
btn_GenCopy.place(x=180, y=130)
lbl_Passwort.place(x=120, y= 200)


root.mainloop()
