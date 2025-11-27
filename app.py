
import streamlit as st
import pandas as pd
from groq import Groq
import os

# Load the CSV
df = pd.read_csv("products_with_images.csv")

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_product(product, user_need):
    prompt = f"""
Explain WHY this product matches the user's needs.

User need: {user_need}

Product:
Name: {product['name']}
Price: {product['price']}
Category: {product['category']}
Features: {product['features']}
Rating: {product['avg_rating']}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# ========== STREAMLIT UI ==========
st.title("🛒 CHOICEMATE") # Using the new suggested name
st.write("An AI companion that helps you pick the best products.")

category = st.selectbox("Choose Category:", sorted(df["category"].unique()))
min_price = st.number_input("Min Budget:", 0, 200000, 500)
max_price = st.number_input("Max Budget:", 0, 200000, 50000)
purpose = st.text_input("Why are you buying this? (e.g., gaming, office, running)")
features = st.text_input("Must-have features (comma separated)")

if st.button("Get Recommendations"):
    must_have = [x.strip().lower() for x in features.split(",") if x.strip()]

    filtered = df[
        (df["category"] == category) &
        (df["price"] >= min_price) &
        (df["price"] <= max_price)
    ]

    st.write(f"### Found {len(filtered)} matching products")

    for _, p in filtered.iterrows():
       
        
        st.write(f"## {p['name']} - ₹{p['price']}")
        st.write(f"⭐ Rating: {p['avg_rating']}")
        st.write("**Features:** " + p["features"])

        # --- NEW PURCHASE LINK DISPLAY ---
        try:
            st.markdown(f"**[🛒 Buy Now on E-Commerce Site]({p['purchase_link']})**")
        except KeyError:
            st.warning("Warning: 'purchase_link' column not found in CSV.")
        # ---------------------------------
        
        explanation = explain_product(p, purpose)
        st.write("### 🤖 Why this product is good for you:")
        st.write(explanation)

        st.write("---")
