import wikiquote
import pandas as pd

PIS = {
    "Lech Kaczyński": 112,
    "Jarosław Kaczyński": 279,
    "Tadeusz Cymański": 43,
    "Marek Kuchciński": 18,
    "Beata Kempa": 23,
    "Adam Hofman": 17,
    "Zbigniew Ziobro": 34,
    "Zbigniew Wassermann": 12,
    "Beata Szydło": 57,
    "Marek Suski": 44,
    "Mateusz Morawiecki": 41,
    "Andrzej Duda": 88,
    "Antoni Macierewicz": 68,
    "Ludwik Dorn": 61,
    "Andrzej Sośnierz": 1,
    "Mariusz Kamiński (ur. 1965)": 7,
}
PO = {
    "Donald Tusk": 151,
    "Ewa Kopacz": 24,
    "Bronisław Komorowski": 101,
    "Małgorzata Kidawa-Błońska": 6,
    "Janusz Palikot": 98,
    "Julia Pitera": 24,
    "Jan Rokita": 36,
    "Grzegorz Schetyna": 26,
    "Róża Thun": 6,
    "Bartosz Arłukowicz": 12,
    "Jerzy Buzek": 12,
    "John Godson": 8,
    "Hanna Gronkiewicz-Waltz": 23,
    "Stefan Niesiołowski": 100,
    "Beata Sawicka": 8,
}


download = lambda name, count: pd.DataFrame(
    wikiquote.quotes(name, lang="pl", max_quotes=count), columns=["Text"]
)

PO_quotes = pd.concat([download(k, v) for k, v in PO.items()])
PO_quotes["Name"] = "PO"

PIS_quotes = pd.concat([download(k, v) for k, v in PIS.items()])
PIS_quotes["Name"] = "PIS"

result = pd.concat([PO_quotes, PIS_quotes])

result.to_csv("politicians.csv", sep="#", index=False)
