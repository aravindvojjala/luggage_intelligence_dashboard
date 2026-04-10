import pandas as pd

df = pd.read_csv("data/raw_data.csv")

df["price"] = df["price"].str.replace(",", "").astype(float)
df = df.dropna(subset=["review"])

df.to_csv("data/clean_data.csv", index=False)