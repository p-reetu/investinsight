# 📊 InvestInsight

**InvestInsight** is a personal investment dashboard and tracker built with Django. It helps you manage, analyze, and visualize your investments across multiple asset types such as **Stocks, Mutual Funds, Crypto, Real Estate, and Gold** — all in one place.

---

## 🚀 Features

- ✅ Add and track investments with real-time insights
- 📈 Interactive dashboard with:
  - Total net worth
  - Investment diversification analysis
  - Gain/Loss insights
  - Short-term and long-term holdings
- 📊 Gold Rate chart (historical data)
- 📥 Auto-calculates Gold value based on current rate
- 🔁 Daily gold rate fetch using **Celery + Django Celery Beat**
- 📅 Tracks investment purchase date
- ✏️ Notes and delete options for each investment

---

## 🛠 Tech Stack

- **Backend**: Django, SQLite/PostgreSQL
- **Frontend**: HTML, Bootstrap, Chart.js
- **Task Queue**: Celery
- **Scheduler**: Django-Celery-Beat
- **APIs**: AMFI API for Mutual Fund NAVs (optional)
- **Containerization**: Docker + Docker Compose

---


## 🧠 How It Works
- Users manually input their investments.
- For Gold, grams are entered and value is auto-calculated based on latest gold rate.
- A separate GoldRates model maintains daily gold prices, fetched automatically.
- Dashboard calculates:
  - Invested vs Current Value
  - Short-term (≤ 1 year) & Long-term (> 1 year) holdings
  - Diversification percentage
  - Charts are rendered using Chart.js.
 
## 🧑‍💻 Author
Built with 💙 by p-reetu.

LinkedIn: [Link](https://www.linkedin.com/in/preeti-manchekar/)
