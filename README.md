# CHOICEMATE – Product Recommendation Assistant

## Overview
CHOICEMATE is an intelligent product recommendation assistant that helps users choose suitable products based on their budget, purpose, category, and required features. It reads from a real dataset and presents product details along with a personalized explanation generated using the Groq LLM (Llama 3.1). The system offers a clean Streamlit interface and is deployed on Streamlit Cloud.

---

## Features & Limitations

### Features
* **Product Discovery:** Select category, define price range, and get matched items.
* **Purpose-based Suggestions:** Users can specify why they're purchasing (gaming, office, running, daily use).
* **Product Details:** Shows Name, Price, Category, Rating, Features, and Purchase link.
* **Personalized Explanation:** Each recommended item comes with an explanation on why it suits the user's needs, generated using Llama 3.1 on Groq.

### Limitations
* Uses a CSV dataset instead of a real database.
* Explanations depend on the LLM quality and input clarity.
* No user login or profile-based personalization.
* Not optimized for large datasets.

---

## Tech Stack & APIs Used

* Programming: Python
* UI: Streamlit
* Libraries: pandas, pillow, groq
* Model & API: Groq API (Llama 3.1 8B Instant)
* Deployment: Streamlit Cloud

**Dataset:** `products_with_images.csv` (Name, category, price, features, rating, purchase link)

---

## Setup & Run Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/choicemate.git](https://github.com/your-username/choicemate.git)
    cd choicemate
    ```
2.  **Install required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Add your API key:**
    Create the secrets file:
    ```bash
    mkdir -p .streamlit
    ```
    Create file:
    ```bash
    nano .streamlit/secrets.toml
    ```
    Paste inside:
    ```toml
    GROQ_API_KEY="your_groq_key_here"
    ```
    Save and exit.

4.  **Run the app:**
    ```bash
    streamlit run app.py
    ```
    The app will open in a browser window.

---

working link :https://akshaya-4924-choicemate-product-recommendation-syste-app-7y0zec.streamlit.app/

## Potential Improvements

* Add image previews for all products.
* Upgrade recommendation logic using embeddings/similarity search.
* Add user login and personalized history.

