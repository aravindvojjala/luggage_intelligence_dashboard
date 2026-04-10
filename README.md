# 🧳 Luggage Intelligence Dashboard

This project analyzes customer luggage reviews and generates actionable business insights using NLP and LLMs.

---

## 🚀 Features

- Sentiment Analysis using TextBlob
- LLM-based Insights Generation (Cerebras - LLaMA model)
- Extracts:
  - Positive Themes
  - Negative Themes
  - Best Brand
  - Worst Brand
  - Hidden Insights

---

## 📁 Project Structure

```
luggage_intelligence_dashboard/
│
├── data/
│ ├── raw_data.csv
│ ├── clean_data.csv
│ └── insights.txt
│
├── analysis/
│ ├── sentiment.py
│ └── llm_insights.py
│
├── app/
│ └── app.py
│
├── scraper/
│ └── scraper.py
│
├── requirements.txt
├── README.md
└── .env.example
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository


git clone https://github.com/aravindvojjala/luggage_intelligence_dashboard

cd luggage_intelligence_dashboard


---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root folder:


CEREBRAS_API_KEY=your_api_key_here


---

## ▶️ How to Run

### Step 1: Run Sentiment Analysis

```commandline
python analysis/sentiment.py
```

---

### Step 2: Generate LLM Insights

```commandline
python analysis/llm_insights.py
```

---

## 📊 Output

The generated insights will be saved in:


data/insights.txt


---

## 🧠 Example Insights

- Customers appreciate durability and design
- Common issues include zipper quality and wheel durability
- Certain brands consistently receive better reviews
- Hidden patterns in customer preferences are identified

---

## 🛠️ Tech Stack

- Python
- Pandas
- TextBlob
- Cerebras LLM (LLaMA 3)
- python-dotenv

---