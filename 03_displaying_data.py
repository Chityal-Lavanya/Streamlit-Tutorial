import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Module 3 - Displaying Data",
    layout="wide"
)

st.title("Displaying Data Dashboard")

# List
st.header("1. List")
courses = ["Python","Java", "React", "Streamlit","Machine Learning"]
st.write(courses)

# Tuple
st.header("2. Tuple")
months = ("January", "February", "March", "April")
st.write(months)

# Dictionary
st.header("3. Dictionary")
student = {
    "Name": "Priya",
    "Age": 21,
    "Branch": "Computer Science",
    "CGPA": 8.9
}
st.write(student)

# Numpy 
st.header("4. Numpy Array")
marks = np.random.randint(60, 100, 10)
st.write(marks)

# Pandas DataFrame
st.header("5. DataFrame")
df = pd.DataFrame({
    "Student": [
        "Rahul",
        "Amit",
        "Priya",
        "Lavanya",
        "Sneha"
    ],
    "Marks": np.random.randint(60,100,5),
    "Attendance": np.random.randint(70,100,5)
})
st.dataframe(df)

# Table
st.header("6. Static Table")
st.table(df)

# JSON
st.header("7. JSON")
st.json(student)

# Metrics
st.header("8. Dashboard Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Students", len(df), "+1")
with col2:
    st.metric("Highest Marks", df["Marks"].max())

# Styled DataFrame
st.header("9. Styled DataFrame")
styled_df = df.style.background_gradient(cmap="Greens")
st.dataframe(styled_df)

# Statistics
st.header("10. Statistics")
st.write("Mean Marks:", df["Marks"].mean())
st.write("Maximum Marks", df["Marks"].max())
st.write("Minimum Marks", df["Marks"].min())