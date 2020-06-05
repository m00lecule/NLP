import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import re
import numpy as np
import demoji

demoji.download_codes()
dfr = pd.read_excel("robert.xlsx")
dfj = pd.read_excel("janusz.xlsx")

result = pd.concat([dfr[["Text", "Name"]], dfj[["Text", "Name"]]])


result["Text"] = result["Text"].apply(lambda x: demoji.replace(str(x), ""))


result["Text"] = result["Text"].apply(
    lambda x: re.sub(r"http\S+|(RT)? ?@[^\s]+ :?|\n|#[^\s]+|\|", "", x)
)

# dfj["Text"] = dfj["Text"].apply(
#     lambda x: re.sub(r"http\S+|(RT)? ?@[^\s]+ :?|\n|#[^\s]+|\|", "", x)
# )

result["Text"] = result["Text"].apply(lambda x: x.rstrip())

result["Text"] = result["Text"].apply(lambda x: x.lstrip())


result["Text"] = result["Text"].apply(lambda x: re.sub(r"$ +", "", x))


result["Text"].replace("", np.nan, inplace=True)

result.dropna(subset=["Text"], inplace=True)


# result = result[~result["Text"].isin([""])]

result.to_csv("quotes1.csv", sep="#", index=False)

# print(result["Text"])
