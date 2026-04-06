# 🛒 Market Basket Recommendation System (FP-Growth)

A smart product recommendation system built using **FP-Growth Algorithm** and **Streamlit UI**, which suggests items based on customer purchase patterns.

--

## 🚀 Live Features

* 🔥 AI-based product recommendations
* 🛒 Market Basket Analysis using FP-Growth
* 🎯 Confidence & Lift based ranking
* 🎨 Beautiful Streamlit UI with cards
* ⚡ Fast (no retraining – uses saved rules)
* 📊 Supports real-world grocery datasets

---

## 🧠 How It Works

1. Transaction dataset is processed
2. FP-Growth algorithm finds frequent itemsets
3. Association rules are generated
4. Rules are saved in `fp_rules.csv`
5. UI loads rules and recommends products

---

## 📁 Project Structure

```
📦 Market-Basket-System
 ┣ 📜 app.py                # Streamlit UI
 ┣ 📜 fp_rules.csv         # Saved association rules
 ┣ 📜 fp_itemsets.csv      # Frequent itemsets (optional)
 ┣ 📜 requirements.txt     # Dependencies
 ┗ 📜 README.md            # Project documentation
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/market-basket-system.git
cd market-basket-system
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📊 Algorithm Used

### 🔹 FP-Growth Algorithm

* Faster than Apriori
* No candidate generation
* Uses FP-Tree structure
* Efficient for large datasets

---

## 📈 Example Output

**Input:**

```
['olive oil']
```

**Output:**

```
mineral water (Score: 1.75)
```

---

## 🎨 UI Features

* Gradient header
* Multi-select product input
* Highlighted CTA button
* Card-based recommendations
* Clean & responsive layout

---

## 🔥 Business Use Cases

* 🛒 Supermarket product placement
* 🎯 Cross-selling & upselling
* 📦 Combo offer generation
* 📊 Customer buying behavior analysis

---

## 🧪 Tech Stack

* Python 🐍
* Pandas
* MLxtend (FP-Growth)
* Streamlit

---

## 🧠 Key Learnings

* Association Rule Mining
* FP-Growth vs Apriori
* Recommendation Systems
* UI + ML Integration
* Data preprocessing techniques

---

## 🎯 Future Improvements

* 📊 Graph visualization
* 🛒 Combo suggestions section
* 🌐 Deployment (Streamlit Cloud / Render)
* 📈 Analytics dashboard

---

## 👨‍💻 Author

**Kanha Patidar**
B.Tech CSIT | Data Science & ML Enthusiast

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share with others

---

## 📌 Final Note

This project demonstrates how **data mining + machine learning + UI** can be combined to build real-world recommendation systems like Amazon or BigBasket.

---
