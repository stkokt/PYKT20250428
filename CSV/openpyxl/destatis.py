import openpyxl as xl

wb = xl.load_workbook('sonderauswertung-nahrungsmittel.xlsx')
ws = wb['Index_2-5-Steller_JD']

# Einlesen der Daten Alternative 1
values = []
for row in ws.iter_rows(min_row=6,max_row=6,min_col=3,max_col=7):
    for cell in row:
        values.append(cell.value)

#print(values)

# Einlesen der Daten Alternative 2
values1 = [[cell.value for cell in row] for row in  ws.iter_rows(min_row=6,max_row=7,min_col=3,max_col=7)]

#print(values1)

# Einlesen der Daten Alternative 3
range = ws['C6': 'G6']

# In range gibt es keine Daten, sondern Zellbezüge
print(range)

# Verschachtelter Loop für die Werte
for cell in range:
    for x in cell:
        print(x.value, end=" ")

values2 = [x.value for x in cell for cell in range]


#print(values2)

wb1 = xl.Workbook('myWorkbook.xlsx')
wb1.save('myWorkbook.xlsx')

import tkinter as tk
from tkinter import filedialog

path = filedialog.askopenfilename(
    title="Excel-Datei öffnen",
    filetypes=(("Excel-Dateien", "*.xlsx"), ("Alle Dateien", "*.*"))
)
print(path)

wb1 = xl.load_workbook(path)
#ws1 = wb1['Blatt']
#ws1.title = "Tabelle 1"
wb1.create_sheet()
sheet = wb1.active
for col_idx, value in enumerate(values, start=1):
    sheet.cell(row=1, column=col_idx, value=value)
wb1.save('myWorkbook.xlsx')