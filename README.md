# 🛒 Market Basket Recommendation System (FP-Growth)

A smart product recommendation system built using **FP-Growth Algorithm** and **Streamlit UI**, deployed live on the cloud.

---

## 🌐 Live Demo

👉 **Try the app here:**
🔗 https://dutxazhxtsec7yrz46w7w.streamlit.app/

---

## 🚀 Features

* 🔥 AI-based product recommendations
* 🛒 Market Basket Analysis using FP-Growth
* 🎯 Confidence & Lift based ranking
* 🎨 Beautiful Streamlit UI with cards
* ⚡ Fast performance (precomputed rules)
* 📊 Real-world dataset support

---

## 🧠 How It Works

1. Transaction dataset is processed
2. FP-Growth algorithm finds frequent itemsets
3. Association rules are generated
4. Rules are saved in `fp_rules.csv`
5. Streamlit UI loads rules and gives recommendations

---

## 📸 Screenshots

> Add your app screenshots here (recommended)

```id="scr1"
![App Screenshot](your-screenshot.png)
```

---

## 📁 Project Structure

```id="scr2"
📦 Market-Basket-System
 ┣ 📜 app.py                # Streamlit UI
 ┣ 📜 fp_rules.csv         # Saved association rules
 ┣ 📜 fp_itemsets.csv      # Frequent itemsets (optional)
 ┣ 📜 requirements.txt     # Dependencies
 ┗ 📜 README.md            # Documentation
```

---

## ⚙️ Installation

```bash id="scr3"
git clone https://github.com/your-username/market-basket-system.git
cd market-basket-system
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash id="scr4"
streamlit run app.py
```

---

## 📊 Algorithm

### 🔹 FP-Growth

* Faster than Apriori
* No candidate generation
* Uses FP-tree
* Efficient for large datasets

---

## 📈 Example

**Input:**

```id="scr5"
['olive oil']
```

**Output:**

```id="scr6"
mineral water (Score: 1.75)
```

---

## 🛒 Business Use Cases

* 🏪 Supermarket product placement
* 🎯 Cross-selling strategies
* 📦 Combo offers
* 📊 Customer behavior analysis

---

## 🧪 Tech Stack

* Python 🐍
* Pandas
* MLxtend
* Streamlit

---

## 🧠 Key Learnings

* Association Rule Mining
* FP-Growth vs Apriori
* Recommendation Systems
* Data preprocessing
* UI + ML integration

---

## 🔮 Future Improvements

* 📊 Graph visualization
* 🛒 Combo suggestions
* 📈 Dashboard analytics
* 🌐 Advanced deployment

---

## 👨‍💻 Author

**Kanha Patidar**
B.Tech CSIT | Data Science Enthusiast

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---

## 📌 Final Note

This project demonstrates how **Machine Learning + Data Mining + UI** can be combined to build real-world recommendation systems like Amazon.

---
