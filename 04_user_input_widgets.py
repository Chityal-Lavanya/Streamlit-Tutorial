import streamlit as st

st.set_page_config(
    page_title="User Input Widgets",
    layout="wide"
)

st.title("User Input Widgets Dashboard")

st.header("Personal Information")

# Text Input
name = st.text_input("Enter Name")

# Text Area
bio = st.text_area("Short Bio")

# Number Input
age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=21
)

# Date Input
dob = st.date_input("Date of Birth")

# Time Input
st.header("Time input")
meeting = st.time_input("Meeting Time")

st.header("Preferences")

# Radio Button
gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)

# SelectBox 
city = st.selectbox(
    "Choose City",
    ["Pune", "Mumbai", "Delhi","Hyderabad"]
)

# Multiselect
skills = st.multiselect(
    "Select Skills",
    ["Python", "Java", "C++", "SQL","React","Streamlit"]
)

# Slider
experience = st.slider(
    "Experience (Years)",
    0,
    20,
    1
)

# Select Slider
level = st.select_slider(
    "Skill Level",
    options=[
        "Beginner",
        "Intermediate",
        "Advanced",
        "Expert"
    ]
)

# color picker
fav_color = st.color_picker(
    "Favorite Color",
    "#0000ff"
)

# Checkbox
newsletter = st.checkbox("Subscribe to newletter")

st.header("Submit")

# Button
if st.button("Submit Details"):
    st.success("Details Submitted Successfully!")

    st.subheader("Summary")

    st.write(f"**Name:** {name}")
    st.write(f"**Bio:** {bio}")
    st.write(f"**Age:** {age}")
    st.write(f"**DOB:** {dob}")
    st.write(f"**Meeting Time:** {meeting}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**City:** {city}")
    st.write(f"**Skills:** {', '.join(skills) if skills else 'None'}")
    st.write(f"**Experience:** {experience} Years")
    st.write(f"**Skill Level:** {level}")
    st.write(f"**Favorite Color:** {fav_color}")
    st.color_picker("Selected Color Preview", fav_color, disabled=True)
    st.write(f"**Newsletter:** {'Yes' if newsletter else 'No'}")














