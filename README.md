# 💰 WiseBudget: A Personal Finance Recommendation System

WiseBudget is a Streamlit-powered app designed to help users take control of their finances by tracking spending, forecasting expenses with machine learning, and receiving personalized savings tips.

---

## 🚀 Features

- 🔐 Secure user login and registration (AES-256 + hashed passwords)
- 🧾 Track financial transactions with category tagging
- 📊 Dashboard comparing budgeted vs. actual expenses
- 🔮 Predict next month's spending using LSTM
- 💡 Smart financial recommendations (hybrid filtering)
- 🌐 Fully deployable on Streamlit Cloud
- ♿️ Accessibility: Colorblind-safe charts, keyboard navigation, and alt-text

---

## 🛠️ Technologies Used

- Python 3.10
- Streamlit
- PostgreSQL
- SQLAlchemy
- TensorFlow (LSTM model)
- bcrypt & cryptography (security)
- pandas, numpy, scikit-learn

---

## 🧰 Installation (Local)

1. Clone the repo:
```bash
git clone https://github.com/your-username/wisebudget.git
cd wisebudget
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```env
DB_USER=yourusername
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
DB_NAME=wisebudget
```

5. Run locally:
```bash
streamlit run app.py
```

---

## ☁️ Streamlit Cloud Deployment

1. Upload to GitHub (exclude `.env`)
2. Add `packages.txt`:
```
python3.10
```
3. Set Streamlit secrets via `Settings > Secrets`:
```toml
[database]
user = "yourusername"
password = "yourpassword"
host = "your-db-host"
port = "5432"
dbname = "wisebudget"
```

4. Deploy at: https://share.streamlit.io

---

## 📝 License

This project is MIT-licensed.

---

## 📷 Screenshots

*(Insert UI screenshots here if desired)*