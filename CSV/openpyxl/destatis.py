import openpyxl as xl

wb = xl.load_workbook('sonderauswertung-nahrungsmittel.xlsx')
ws = wb['Index_2-5-Steller_JD']
values = []
for row in ws.iter_rows(min_row=6,max_row=6,min_col=3,max_col=7):
    for cell in row:
        values.append(cell.value)

v1 = [[cell.value for cell in row] for row in  ws.iter_rows(min_row=6,max_row=7,min_col=3,max_col=7)]

print(v1)

range = ws['C6': 'G6']

for cell in range:
    for x in cell:
        print(x.value)

import tkinter as tk
from tkinter import filedialog

path = filedialog.askopenfilename(
    title="Excel-Datei öffnen",
    filetypes=(("Excel-Dateien", "*.xlsx"), ("Alle Dateien", "*.*"))
)
print(path)

# wb1 = xl.Workbook('myWorkbook.xlsx')
wb1 = xl.load_workbook(path)
#ws1 = wb1['Blatt']
#ws1.title = "Tabelle 1"
wb1.create_sheet()
wb1.save('myWorkbook.xlsx')