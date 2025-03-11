import pandas as pd

df = pd.read_csv('data_small/TG_STAID000001.txt', skiprows=20)
df["TG"] = df['   TG'].loc[df['   TG'] != -9999] / 10
df["    DATE"] = df["    DATE"].astype(str)
df = df[["    DATE", 'TG']]
df = df[df["    DATE"].str.startswith(str(1860))]
print(df)
