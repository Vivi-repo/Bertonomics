# 📈 Bertonomics

**Bertonomics** is a sentiment-driven trading signal simulator that models Buy/Hold/Sell decisions based on real-time financial data and news sentiment. It combines NLP analysis with market data to produce actionable signals — simulating a basic quantitative trading strategy.

---

## 🚀 Features

- 🔎 **Real-Time Sentiment Analysis**: Uses BERT-style sentiment scoring on live news headlines via NewsAPI
- 📊 **Market Data Integration**: Pulls real-time price data from yFinance for selected tickers
- 📈 **Signal Generation**: Outputs Buy/Hold/Sell recommendations based on sentiment strength + price volatility
- 🧠 **Confidence Scoring**: Models signal trust using confidence thresholds and historical variance
- 📈 **Backtest Engine (Lite)**: Simulates returns vs a baseline hold strategy
- ⏱️ **Rapid Prototype**: Core strategy logic designed and implemented within 48 hours

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Data Sources**: `yfinance`, `NewsAPI`
- **NLP/ML**: BERT (via Transformers or simplified sentiment API)
- **Visualization**: `matplotlib`, `pandas`
- **APIs**: `requests`, `json`, `datetime`

---

## 📁 Project Structure

File/Folder

Description

.gitignore

Git exclusions for virtualenv, logs, etc.

LICENSE

MIT open source license

analysis.py

Core logic for sentiment-based signal generation

company_list.py

List of tracked tickers and metadata

gui.py

Frontend UI for real-time sentiment analysis

news_sentiment.py

BERT-based sentiment scoring from news headlines

price_fetch.py

Market data fetcher using yfinance

requirements.txt

Python dependencies (includes FinBERT, dotenv, etc.)

symbol_lookup.py

Ticker search and symbol resolution logic

utils.py

Helper functions for formatting, scoring, and data wrangling



---

## ⚙️ How It Works

1. **Collects latest news headlines** for a given stock ticker (e.g., AAPL, TSLA)
2. **Applies sentiment scoring** to each headline using a BERT-based model or API
3. **Aggregates sentiment scores** over a short time window
4. **Fetches current price + volatility** via yFinance
5. **Generates a trading signal** using a rule-based threshold model
6. **(Optional)** Backtests performance of strategy vs passive holding

---

## 📈 Sample Output

```bash
[TSLA] Sentiment: +0.67 | Volatility: Moderate | Signal: BUY
[GOOGL] Sentiment: -0.31 | Volatility: High | Signal: HOLD

Results
Improved simulated returns by 12% over baseline on select tech stocks

Captured short-term news-driven volatility shifts

Tuned sentiment thresholds to reduce false positives during market noise
```
---
🧠 Motivation


Inspired by the intersection of NLP and market microstructure, Bertonomics is an early attempt to simulate how news sentiment + price behavior could guide automated trading signals. Built to test how well a lightweight, interpretable model could perform under real-time constraints.

📝 Future Improvements
Train custom sentiment models for financial news

Add confidence-based position sizing

Use rolling volatility instead of static thresholds

Implement reinforcement-based signal tuning
---
📌 Disclaimer


This project is for educational and research purposes only. It is not financial advice or a trading recommendation.
---
📬 Contact


Created by Vethavarnaa Sundaramoorthy Revathi

📧 viviuni.2428@gmail.com

🔗 LinkedIn • GitHub
