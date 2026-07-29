import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(
    page_title="Database Integration",
    layout="wide"
)

st.title("🎓 Student Management System")
st.markdown("### Streamlit + MySQL CRUD Operations")

# Database Connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="" 
    )

# Create Database & Table
def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS student1_db")
    cursor.execute("USE student1_db")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            department VARCHAR(100),
            email VARCHAR(100),
            phone VARCHAR(20)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

initialize_database()

# Connect Student Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      
        database="student1_db"
    )

# CREATE
def add_student(name, age, department, email, phone):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO students
    (name, age, department, email, phone)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (name, age, department, email, phone)
    )

    conn.commit()

    cursor.close()
    conn.close()

# READ
def get_students():

    conn = connect_db()

    query = "SELECT * FROM students"

    df = pd.read_sql(query, conn)

    conn.close()

    return df

# UPDATE
def update_student(id, name, age, department, email, phone):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    UPDATE students
    SET
    name=%s,
    age=%s,
    department=%s,
    email=%s,
    phone=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (
            name,
            age,
            department,
            email,
            phone,
            id
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

# DELETE
def delete_student(id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

# SEARCH
def search_student(keyword):

    conn = connect_db()

    query = f"""
    SELECT * FROM students
    WHERE
    name LIKE '%{keyword}%'
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

# Sidebar Menu
menu = st.sidebar.radio(
    "Navigation",
    [
        "Add Student",
        "View Students",
        "Update Student",
        "Delete Student",
        "Search Student"
    ]
)

# Add Student
if menu == "Add Student":

    st.header("➕ Add Student")

    with st.form("add_form"):

        name = st.text_input("Name")

        age = st.number_input(
            "Age",
            18,
            60
        )

        department = st.text_input("Department")

        email = st.text_input("Email")

        phone = st.text_input("Phone")

        submit = st.form_submit_button(
            "Add Student"
        )

        if submit:

            if name == "" or email == "":
                st.error("Name and Email are required.")

            else:

                add_student(
                    name,
                    age,
                    department,
                    email,
                    phone
                )
                st.success("Student Added Successfully")

# View Students
elif menu == "View Students":

    st.header("📋 Student Records")

    df = get_students()

    st.dataframe(
        df,
        use_container_width=True
    )

# Update Student
elif menu == "Update Student":

    st.header("✏ Update Student")

    id = st.number_input(
        "Student ID",
        1,
        step=1
    )

    name = st.text_input("New Name")

    age = st.number_input(
        "New Age",
        18,
        60
    )

    department = st.text_input(
        "New Department"
    )

    email = st.text_input(
        "New Email"
    )

    phone = st.text_input(
        "New Phone"
    )

    if st.button("Update"):

        update_student(
            id,
            name,
            age,
            department,
            email,
            phone
        )

        st.success("Student Updated Successfully")

# Delete Student
elif menu == "Delete Student":

    st.header("🗑 Delete Student")

    id = st.number_input(
        "Student ID",
        1,
        step=1
    )

    if st.button("Delete"):

        delete_student(id)

        st.success("Student Deleted Successfully")

# Search Student
elif menu == "Search Student":

    st.header("🔍 Search Student")

    keyword = st.text_input(
        "Enter Student Name"
    )

    if keyword:
        df = search_student(keyword)

        st.dataframe(
            df,
            use_container_width=True
        )