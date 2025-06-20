import pandas as pd
import numpy as np
import time

# Erstellen einer großen Liste von Zahlen
# data = list(range(1, 1000001))

# # Startzeit messen
# start_time = time.time()

# # Summierung mit normalem Python
# total = sum(data)

# # Endzeit messen
# end_time = time.time()

# # Zeitdifferenz berechnen
# print(f"Summe: {total}")
# print(f"Zeit mit normalem Python: {end_time - start_time} Sekunden")

# PANDAS

# Erstellen einer großen Liste von Zahlen
# data = list(range(1, 1000001))

# # Erstellen eines Pandas DataFrame
# df = pd.DataFrame(data, columns=["Numbers"])

# # Startzeit messen
# start_time = time.time()

# # Summierung mit Pandas
# total = df["Numbers"].sum()

# # Endzeit messen
# end_time = time.time()

# # Zeitdifferenz berechnen
# print(f"Summe: {total}")
# print(f"Zeit mit Pandas: {end_time - start_time} Sekunden")

print("\nErstellen einer Series\n")
# Erstellen einer Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

print("\nErstellen eines DataFrame\n")
# Erstellen eines DataFrame
data = {
    "Name": ["Stefan", "Micha", "Wasim", "Ali"],
    "Alter": [55, 30, 35, 35],
    "Stadt": ["Berlin", "München", "Hamburg", "München"]
}

df = pd.DataFrame(data)

df.to_csv("datei.csv", index=False)
df = pd.read_csv("datei.csv")

print(df)

print("\nEine einzelne Spalte auswählen\n")
# Eine einzelne Spalte auswählen
namen = df["Name"]
print(namen)

print("\nMehrere Spalten auswählen\n")
# Mehrere Spalten auswählen
subset = df[["Name", "Alter"]]
print(subset)

print("\nFilter\n")
# Zeilen filtern, bei denen das Alter größer als 25 ist
filter_df = df[df["Alter"] > 30]
print(filter_df)

print("\nSpalte hizufügen\n")
df["Neue_Spalte"] = [10, 20, 30, 40]
print(df)

print("\nSpalte entfernen\n")
df = df.drop("Neue_Spalte", axis=1)
print(df)

print("\nWert ändern\n")
df.loc[df["Name"] == "Micha", "Alter"] = 32
print(df)

print("\nGruppieren\n")
gruppiert = df.groupby("Stadt")
print(gruppiert)

anzahl = gruppiert.size()
print(anzahl)


