import pandas as pd
from datetime import datetime

df = pd.read_csv("data_small/TG_STAID000010.txt", skiprows=20, parse_dates=["    DATE"])
df["TG"] = df['   TG'].loc[df['   TG'] != -9999]/10

date = '1860-01-01'
temperature = df["TG"].loc[df['    DATE'] == date].squeeze()
print(df)
print(temperature)
date = '20030225'
date = datetime.strptime(date, "%Y-%m-%d").date()
print(date)
