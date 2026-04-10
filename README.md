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
## STEP-BY-STEP EXECUTION FLOW
1. Run scraper → raw_data.csv
2. Run clean → clean_data.csv
3. Run sentiment → brand_summary.csv
4. Run LLM insights → insights.txt
5. Run Streamlit → Dashboard
---

## ▶️ How to Run

### Step 1: Run scraper
```commandline
python scraper/scraper.py
```

### Step 2: Clean data
```commandline
python analysis/clean.py
```

### Step 3: Run Sentiment Analysis
```commandline
python analysis/sentiment.py
```

### Step 4: Generate LLM Insights
```commandline
python analysis/llm_insights.py
```

### Step 5: Run dashboard
```commandline
streamlit run app/app.py
```

---

## 📊 Output

The generated insights will be saved in:
data/insights.txt
The generated insights will be displayed in UI

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

## 📌 Notes

- Ensure API key is valid before running
- Do not share `.env` file publicly
- Works locally (no deployment required)

---

## 🎯 Future Improvements

- Streamlit Dashboard for visualization
- Real-time review analysis
- Deployment using cloud platforms

---

## 👨‍💻 Author

Aravind
