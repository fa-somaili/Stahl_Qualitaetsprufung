# Stahl-Qualitätsprüfung {Optische Fehlerauswertung}

Python-Skript zur automatisierten Auswertung optischer Kameraprüfdaten von Stahlbauteilen auf Basis des öffentlichen UCI-Industriedatensatzes (Steel Plates Faults, 1.941 Datensätze).

## Funktionsweise
1. Datenimport: Lädt 1.941 Prüfdatensätze inklusive Materialstärke (Steel_Plate_Thickness), Stahlsorte (A300, A400) und binären Kameraprüfmerkmalen direkt über ucimlrepo.
2. Klassifizierung (i.O. / n.i.O.): Prüft jeden Datensatz auf 7 definierte Oberflächen- und Materialfehler (Pastry, Z_Scratch, K_Scratch, Stains, Dirtiness, Bumps, Other_Faults) und ordnet den jeweiligen Fehlerklartext zu.
3. Berichtsexport: Gibt die Gesamtanzahl geprüfter Teile sowie die Fehlerverteilung im Terminal aus und erstellt die Excel-Datei Stahl_Optische_QA_Auswertung.xlsx mit zwei Tabellenblättern (Fehler_Statistik und Pruefprotokoll_Gesamt).

## Voraussetzungen & Ausführung
pip install -r requirements.txt
python stahl_qualitaetspruefung.py


