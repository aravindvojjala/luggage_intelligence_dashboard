import pandas as pd
from textblob import TextBlob

df = pd.read_csv("data/clean_data.csv")

df["sentiment"] = df["review"].apply(lambda x: TextBlob(x).sentiment.polarity)

summary = df.groupby("brand").agg({
    "price": "mean",
    "sentiment": "mean",
    "review": "count"
}).reset_index()

summary.to_csv("data/brand_summary.csv", index=False)
df.to_csv("data/clean_data.csv", index=False)