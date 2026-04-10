from dotenv import load_dotenv
from openai import OpenAI
from cerebras.cloud.sdk import Cerebras
import pandas as pd
import os

load_dotenv()
# OpenAI
# Cerebras
client = OpenAI(
    api_key=os.getenv("CEREBRAS_API_KEY"),
    base_url="https://api.cerebras.ai/v1"
)

df = pd.read_csv("data/clean_data.csv")

sample_reviews = df["review"].sample(min(50, len(df))).tolist()

prompt = f"""
You are a market intelligence analyst.

Return structured output with headings:

1. Positive Themes
2. Negative Themes
3. Best Brand (with reason)
4. Worst Brand (with reason)
5. Hidden Insights (3 points)

Reviews:
{sample_reviews}
"""

response = client.chat.completions.create(
    model="llama3.1-8b",
    messages=[{"role": "user", "content": prompt}]
)

insights = response.choices[0].message.content

with open("data/insights.txt", "w") as f:
    f.write(insights)