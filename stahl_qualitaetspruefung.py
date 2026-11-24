import pandas as pd
from ucimlrepo import fetch_ucirepo

datensatz = fetch_ucirepo(id=198)
df = pd.concat([datensatz.data.features, datensatz.data.targets], axis=1)

fehler_spalten = list(datensatz.data.targets.columns)

def bestimme_fehler(row):
    gefunden = [spalte for spalte in fehler_spalten if row[spalte] == 1]
    if len(gefunden) == 0:
        return pd.Series(["i.O.", "-"])
    return pd.Series(["n.i.O.", ", ".join(gefunden)])

df[["Prüfstatus", "Fehlerart"]] = df.apply(bestimme_fehler, axis=1)

gesamt = len(df)
ausschuss_df = df[df["Prüfstatus"] == "n.i.O."]
fehler_verteilung = df[fehler_spalten].sum().reset_index()
fehler_verteilung.columns = ["Fehlerart", "Anzahl"]

print(f"Geprüfte Stahl-Prüflinge: {gesamt} | Fehlerhaft (n.i.O.): {len(ausschuss_df)}")
print(fehler_verteilung.to_string(index=False))

with pd.ExcelWriter("Stahl_Optische_QA_Auswertung.xlsx", engine="openpyxl") as writer:
    fehler_verteilung.to_excel(writer, sheet_name="Fehler_Statistik", index=False)
    df[["Steel_Plate_Thickness", "TypeOfSteel_A300", "TypeOfSteel_A400", "Prüfstatus", "Fehlerart"]].to_excel(
        writer, sheet_name="Pruefprotokoll_Gesamt", index=False
    )


