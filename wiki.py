import wikiquote
import pandas as pd


politicans = ["Donald Tusk", "Lech Kaczyński"]


df = pd.DataFrame(
    wikiquote.quotes("Donald Tusk", lang="pl", max_quotes=None), columns=["Text"]
)

df["Name"] = "Donald Tusk"


df1 = pd.DataFrame(
    wikiquote.quotes("Lech Kaczyński", lang="pl", max_quotes=None), columns=["Text"]
)

df1["Name"] = "Lech Kaczyński"


result = pd.concat([df1, df])

result.to_csv("politicians.csv", sep="#", index=False)
