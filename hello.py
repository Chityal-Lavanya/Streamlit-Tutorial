import streamlit as st

st.set_page_config(
    page_title="Hello Streamlit",
    layout="centered"
)
st.title("Hello Streamlit")

st.write("Welcome to your first Streamlit application.")

name = st.text_input("Enter your name")
if st.button("Submit"):
    if name: 
        st.success(f"Hello, {name}! Welcome to Streamlit.")
    else:
        st.warning("Please enter your name.")