import streamlit as st

st.set_page_config(
    page_title="Session state",
    layout="wide"
)

st.title("Smart Task Manager (Session State Demo)")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "counter" not in st.session_state:
    st.session_state.counter = 0

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Login 
st.sidebar.header("Login")

if not st.session_state.logged_in:
    username = st.sidebar.text_input("Username")
    passward = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username == "admin" and passward == "1234":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login Successful!")
        else:
            st.error("Invalid Username or Password")

else:
    st.sidebar.success(f"Welcome {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

# Counter
st.header("Persistent Counter")

col1, col2 = st.columns(2)

with col1:
    if st.button("Increase Counter"):
        st.session_state.counter +=1

with col2:
    if st.button("Reset Counter"):
        st.session_state.counter = 0

st.metric("Current Counter", st.session_state.counter)
st.divider()

# Task Manager
st.header("Task Manager")

task = st.text_input("Enter New Task")

if st.button("Add Task"):
    if task.strip():
        st.session_state.tasks.append(task)

st.subheader("Current Tasks")

if st.session_state.tasks:
    for i, item in enumerate(st.session_state.tasks, start=1):
        st.write(f"{i}. {item}")

else:
    st.info("No tasks added yet.")

st.header("Session State Data")
st.write(st.session_state)
st.divider()

if st.button("Clear Entire Session"):
    st.session_state.clear()
    st.rerun()