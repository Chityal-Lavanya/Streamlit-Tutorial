import streamlit as st
import time

st.set_page_config(
    page_title="Layout and Containers",
    layout="wide"
)

st.title("Layout & Containers Dashboard")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose Section",
    ["Dashboard","Profile","Help"]
)

st.divider()

# Columns
st.header("Dashboard Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Students", "250")
with col2:
    st.metric("Courses", "18")
with col3:
    st.metric("Projects", "42")

st.divider()

# Container
with st.container():
    st.header("👤User Information")
    st.write("**Name:** Lavanya Chityal")
    st.write("**Role:** Python Developer")
    st.write("**Experience:** 2 Years")

st.divider()

# Tabs
tab1, tab2, tab3 = st.tabs(
    ["Profile","Skills", "Projects"]
)
with tab1:
    st.write("Software Developer passionate about Python and Streamlit.")

with tab2:
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- SQL")

with tab3:
    st.write("Student Management System")
    st.write("Sales Dashboard")
    st.write("Weather App")

st.divider()

# Expander
with st.expander("Frequently Asked Questions"):
    st.write("**Q:** What is Streamlit?")
    st.write("A: A Python framework for building data apps.")

    st.write("**Q:** Why use Layout Components?")
    st.write("A: They make applications organized and user-friendly.")

st.divider()

# Empty Placeholder
st.header("Live Status")
placeholder = st.empty()
placeholder.info("Loading dashboard...")
time.sleep(2)
placeholder.success("Dashboard loaded Successfully!")

# Divider
st.divider()
st.success("Layout & Containers Demonstration Completed!")