import streamlit as st

st.set_page_config(
    page_title="Forms",
    layout="centered"
)

st.title("Student Registration & Feedback System")
with st.form("student_registration", clear_on_submit=True):
    st.subheader("Student Details")

    name = st.text_input("Full Name")

    email = st.text_input("Email Address")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=18
    )

    gender = st.radio(
        "Gender",
        ["Male", "Female", "Other"]
    )

    course = st.selectbox(
        "Course",
        [
            "Python",
            "Java",
            "Data Science",
            "Web Development"
        ]
    )

    skills = st.multiselect(
        "Skills",
        [
            "Python",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript",
            "Streamlit"
        ]
    )

    feedback = st.text_area("Feedback")

    agree = st.checkbox(
        "I confirm that the above information is correct."
    )

    submit = st.form_submit_button("Register")

if submit:
    if not name.strip():
        st.error("Name is Required.")

    elif not email.strip():
        st.error("Email is required.")

    elif age < 18:
        st.warning("Student must be at least 18 years old.")

    elif not agree:
        st.warning("Please confirm the declaration")

    else:
        st.success("🎉 Registration Successful!")

        st.subheader("Submitted Information")

        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Course:** {course}")
        st.write(
            f"**Skills:** {', '.join(skills) if skills else 'None'}"
        )
        st.write(f"**Feedback:** {feedback if feedback else 'No feedback provided'}")