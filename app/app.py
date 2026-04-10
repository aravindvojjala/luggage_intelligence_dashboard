import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/clean_data.csv")
summary = pd.read_csv("data/brand_summary.csv")

st.set_page_config(layout="wide")
st.title("🧳 Luggage Competitive Intelligence Dashboard")

# Filters
brands = st.multiselect("Select Brands", df["brand"].unique(), default=df["brand"].unique())
df = df[df["brand"].isin(brands)]

# Overview
st.subheader("Overview")
col1, col2, col3 = st.columns(3)

col1.metric("Total Brands", df["brand"].nunique())
col2.metric("Total Products", df["product"].nunique())
col3.metric("Total Reviews", len(df))

# Charts
st.subheader("Brand Comparison")

fig1 = px.bar(summary, x="brand", y="price", title="Average Price")
fig2 = px.bar(summary, x="brand", y="sentiment", title="Sentiment Score")

st.plotly_chart(fig1)
st.plotly_chart(fig2)

st.dataframe(summary)

# Product Drilldown
st.subheader("Product Drilldown")
product = st.selectbox("Select Product", df["product"].unique())
st.write(df[df["product"] == product])

# LLM Insights
st.subheader("🤖 AI Insights")

try:
    with open("data/insights.txt", "r") as f:
        st.write(f.read())
except:
    st.warning("Run llm_insights.py to generate insights")