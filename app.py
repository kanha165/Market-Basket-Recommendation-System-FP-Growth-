import streamlit as st
import pandas as pd
import ast

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Market Basket System", layout="wide")

# -------------------------------
# LOAD RULES
# -------------------------------
@st.cache_data
def load_rules():
    rules = pd.read_csv("fp_rules.csv")

    def clean_frozenset(x):
        x = x.replace("frozenset(", "").replace(")", "")
        return list(ast.literal_eval(x))

    rules['antecedents'] = rules['antecedents'].apply(clean_frozenset)
    rules['consequents'] = rules['consequents'].apply(clean_frozenset)

    return rules

rules = load_rules()

# -------------------------------
# GET ALL UNIQUE ITEMS
# -------------------------------
items = sorted(list(set([item for sublist in rules['antecedents'] for item in sublist])))

# -------------------------------
# RECOMMEND FUNCTION
# -------------------------------
def recommend_fp(rules, user_items):
    results = {}

    user_items = [item.strip().lower() for item in user_items]

    for _, row in rules.iterrows():
        antecedent = [i.strip().lower() for i in row['antecedents']]
        consequent = row['consequents']

        score = row['confidence'] * row['lift']

        if any(item in antecedent for item in user_items):
            for item in consequent:
                if item not in results:
                    results[item] = score
                else:
                    results[item] += score

    return sorted(results.items(), key=lambda x: x[1], reverse=True)

# -------------------------------
# HEADER UI
# -------------------------------
st.markdown("""
<div style='text-align:center; padding:25px; border-radius:15px;
background: linear-gradient(90deg, #1f77b4, #17becf); color:white'>
    <h1>🛒 Market Basket Recommendation System</h1>
    <p>Smart AI-based product suggestions using FP-Growth</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------------
# INPUT SECTION
# -------------------------------
st.markdown("### 🛍️ Select Products")

selected_items = st.multiselect(
    "Choose items:",
    items,
    placeholder="Select items like milk, bread..."
)

# -------------------------------
# BUTTON STYLE (ADD ABOVE BUTTON)
# -------------------------------
st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(90deg, #ff7e5f, #feb47b);
    color: white;
    font-size: 18px;
    padding: 12px 30px;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# BUTTON SECTION
# -------------------------------
st.markdown("### 🚀 Click below to generate smart recommendations")

if st.button("✨ Get Recommendations"):

    if not selected_items:
        st.warning("⚠️ Please select at least one item")

    else:
        recommendations = recommend_fp(rules, selected_items)

        # ❌ Remove already selected items
        recommendations = [
            (item, score) for item, score in recommendations 
            if item not in selected_items
        ]

        st.markdown("## 🎯 Recommended Products")

        if len(recommendations) == 0:
            st.error("❌ No recommendations found")
        else:
            cols = st.columns(3)

            for i, (item, score) in enumerate(recommendations[:9]):
                with cols[i % 3]:
                    st.markdown(f"""
                    <div style='padding:18px; border-radius:15px;
                    background:linear-gradient(135deg,#2ca02c,#6fdc8c);
                    color:white; text-align:center;
                    box-shadow:0px 6px 20px rgba(0,0,0,0.2);
                    transition:0.3s'>
                        <h3>🛒 {item}</h3>
                        <p style='font-size:14px;'>Score: {round(score,2)}</p>
                    </div>
                    """, unsafe_allow_html=True)
# -------------------------------
# FOOTER
# -------------------------------
st.write("")
st.markdown("---")
st.markdown("<center>🔥 Built using FP-Growth | Kanha Project</center>", unsafe_allow_html=True)