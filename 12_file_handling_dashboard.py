import streamlit as st
import pandas as pd
import json
from PIL import Image
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="File Handling",
    layout="wide"
)

st.title(" Universal File Manager Dashboard ")

option = st.sidebar.selectbox(
    "Choose File Type",
    ["CSV", "Excel", "JSON", "Image", "PDF"]
)

uploaded_file = st.file_uploader(
    "Upload Your File",
    type=["csv", "xlsx", "json", "png", "jpg", "jpeg", "pdf"]
)

if uploaded_file:
    if option == "CSV":
        df = pd.read_csv(uploaded_file)
        st.subheader("CSV Preview")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download CSV",
            csv,
            "processed_data.csv",
            "text/csv"
        )
    elif option == "EXcel":
        df = pd.read_excel(uploaded_file)
        st.subheader("Excel Preview")
        st.dataframe(df)

    elif option == "JSON":
        data = json.load(uploaded_file)
        st.subheader("JSON Preview")
        st.json(data)

    elif option == "Image":
        image = Image.open(uploaded_file)
        st.subheader("Image Preview")
        st.image(image, use_container_width=True)

    elif option == "PDF":
        reader = PdfReader(uploaded_file)

        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        st.subheader("Extracted PDF Text")
        st.text_area(
            "Content",
            text,
            height=400
        )
        