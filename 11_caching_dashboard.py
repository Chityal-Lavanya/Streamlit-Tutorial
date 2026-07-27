import streamlit as st
import pandas as pd
import time
import requests

st.set_page_config(
    page_title="Module 11 - Caching",
    layout="wide"
)

st.title(" Caching Dashboard")

# Cache Data Example
@st.cache_data
def load_dataset():
    time.sleep(3) 
    return pd.DataFrame({
        "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
        "Sales": [120, 180, 95, 75]
    })

# Cache Resource Example
@st.cache_resource
def load_model():
    time.sleep(5) 
    return "Sales Prediction Model Loaded"

# API Cache Example
@st.cache_data(ttl=300)
def fetch_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=10
    )
    return response.json()

# Dataset Section
st.header("📊 Cached Dataset")

start = time.time()
df = load_dataset()
elapsed = time.time() - start

st.dataframe(df)
st.success(f"Dataset loaded in {elapsed:.2f} seconds")

# Resource Section
st.header("🤖 Cached Resource")

start = time.time()
model = load_model()
elapsed = time.time() - start

st.success(model)
st.info(f"Model loaded in {elapsed:.2f} seconds")

# API Section
st.header("🌐 Cached API Data")

users = fetch_users()

st.write("First 5 Users")
st.table(pd.DataFrame(users)[["id", "name", "email"]].head())

# Performance Info
st.header(" Performance Optimization")

st.markdown("""
- `st.cache_data` stores data like DataFrames and API responses.
- `st.cache_resource` stores long-lived resources like models and database connections.
- Reload the app or interact with widgets to observe that cached operations complete much faster after the first execution.
""")

# Clear Cache
if st.button("Clear Cached Data"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success("All caches have been cleared.")