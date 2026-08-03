import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="University Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp{
background-image:linear-gradient(
135deg,
#eef2ff,
#ffffff,
#dbeafe
);
}

h1,h2,h3{
font-family:Verdana;
color:#2563EB;
}

div[data-testid="metric-container"]{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,.2);
}

.stButton>button{

background:#2563EB;
color:white;
border-radius:10px;
height:45px;
width:100%;
font-size:18px;
}

.profile{

background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 8px gray;
text-align:center;
}

.footer{

text-align:center;
font-size:18px;
padding:20px;
color:gray;
}

</style>
""",
unsafe_allow_html=True)

# Sidebar
# st.sidebar.image("images/logo.png", width=150)
menu=st.sidebar.radio(
"📚 Navigation",
[
"Dashboard",
"Students",
"Analytics",
"Settings"
]
)

st.sidebar.markdown("---")

st.sidebar.success("🎓 Streamlit Module 17")

# Dashboard
if menu=="Dashboard":

    st.title("🎓 University Analytics Dashboard")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Students","2500","+120")
    c2.metric("Faculty","180","+10")
    c3.metric("Courses","75","+5")
    c4.metric("Attendance","94%","+2%")

    st.divider()

    left,right=st.columns([2,1])

    with left:

        st.subheader("📈 Student Growth")

        df=pd.DataFrame({
            "Year":[2021,2022,2023,2024,2025],
            "Students":[1200,1500,1800,2100,2500]
        })

        st.line_chart(
            df,
            x="Year",
            y="Students"
        )

    with right:

        st.markdown("""
        <div class="profile">

        <h2>👤 Admin</h2>
        <p>Name : Lavanya</p>
        <p>Role : Administrator</p>
        <p>Status : 🟢 Online</p>

        </div>

        """,
        unsafe_allow_html=True)

    st.divider()

    st.subheader("🎨 Theme Colors")

    c1,c2,c3,c4=st.columns(4)

    c1.success("Success")
    c2.info("Information")
    c3.warning("Warning")
    c4.error("Error")

    st.divider()

    st.subheader("😊 Icons")
    st.write("🎓 📊 📁 📈 👨‍🎓 👩‍🏫 💻 📚 ⚙ 🔒 ❤️ ⭐")

    st.divider()

    st.subheader("🔘 Buttons")

    col1,col2,col3=st.columns(3)

    col1.button("Save")
    col2.button("Update")
    col3.button("Delete")

elif menu=="Students":

    st.title("👨‍🎓 Student Records")

    data=pd.DataFrame({

        "Name":["Priya","Neha","Laya","Sneha"],
        "Marks":[91,87,76,95],
        "Attendance":[93,95,90,98]

    })
    st.dataframe(data,use_container_width=True)

elif menu=="Analytics":

    st.title("📊 Analytics")

    chart=pd.DataFrame(
        np.random.randint(
            10,
            100,
            size=(20,3)
        ),
        columns=[
            "Python",
            "Java",
            "C++"
        ]
    )

    st.area_chart(chart)
    st.bar_chart(chart)

elif menu=="Settings":

    st.title("⚙ Settings")

    theme=st.selectbox(
        "Theme",
        ["Light Mode","Dark Mode"]

    )

    font=st.selectbox(
        "Font",
        ["Sans Serif","Serif", "Monospace"]
    )

    color=st.color_picker(
        "Primary Color",
        "#2563EB"
    )

    st.write("Selected Theme :",theme)
    st.write("Selected Font :",font)
    st.write("Primary Color :",color)

st.markdown("""
<div class="footer">
Made with ❤️ using Streamlit

</div>

""", unsafe_allow_html=True)