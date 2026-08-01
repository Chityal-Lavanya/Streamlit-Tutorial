import streamlit as st
import hashlib

st.set_page_config(
    page_title="Authentication System",
    layout="wide"
)

st.title("🔐 Secure Authentication System")

# Session Initialization
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = ""

# Password Hash Function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Sidebar Menu
menu = st.sidebar.selectbox(
    "Navigation",
    ["Register", "Login", "Dashboard"]
)

# Register
if menu == "Register":

    st.header("📝 User Registration")
    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    confirm = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Register"):

        if not username or not password:
            st.error("All fields are required.")

        elif password != confirm:
            st.error("Passwords do not match.")

        elif username in st.session_state.users:
            st.warning("Username already exists.")

        else:
            st.session_state.users[username] = hash_password(password)
            st.success("Registration Successful!")

# Login
elif menu == "Login":

    st.header("🔑 User Login")
    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        hashed = hash_password(password)

        if (
            username in st.session_state.users
            and st.session_state.users[username] == hashed
        ):
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success("Login Successful!")

        else:
            st.error("Invalid Username or Password")

# Dashboard
elif menu == "Dashboard":

    if st.session_state.logged_in:

        st.success(
            f"Welcome, {st.session_state.current_user}!"
        )

        st.subheader("📊 Protected Dashboard")

        st.write("Only authenticated users can view this page.")

        st.info(
            "This login state is maintained using Streamlit Session State."
        )

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.current_user = ""
            st.success("Logged Out Successfully")
            st.rerun()

    else:
        st.error("Please log in to access the dashboard.")