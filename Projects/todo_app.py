import streamlit as st
import pandas as pd
import json
from datetime import date

st.set_page_config(
    page_title="To-Do Task Manager",
    page_icon="✅",
    layout="wide"
)

st.title("📝 To-Do Task Manager")
st.write("Manage your daily tasks efficiently.")

# Session State
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add Task
st.header("➕ Add New Task")

col1, col2 = st.columns(2)
with col1:
    task = st.text_input("Task Title")
    description = st.text_area("Description")
    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

with col2:
    due = st.date_input(
        "Due Date",
        date.today()
    )
    category = st.selectbox(
        "Category",
        ["Study", "Office", "Personal", "Shopping", "Other"]
    )
    completed = st.checkbox("Completed")

if st.button("Add Task", use_container_width=True):

    if task:
        st.session_state.tasks.append({
            "Task": task,
            "Description": description,
            "Priority": priority,
            "Due Date": str(due),
            "Category": category,
            "Completed": completed
        })
        st.success("Task Added Successfully!")
    else:
        st.error("Task name required!")

st.divider()

# Search & Filter
st.header("🔍 Search Tasks")

col1, col2 = st.columns(2)

search = col1.text_input("Search Task")

filter_priority = col2.selectbox(
    "Priority Filter",
    ["All", "High", "Medium", "Low"]
)
tasks = st.session_state.tasks

if search:
    tasks = [
        t for t in tasks
        if search.lower() in t["Task"].lower()
    ]

if filter_priority != "All":
    tasks = [
        t for t in tasks
        if t["Priority"] == filter_priority
    ]

# Statistics
total = len(st.session_state.tasks)

completed_count = sum(
    task["Completed"]
    for task in st.session_state.tasks
)

pending = total - completed_count

c1, c2, c3 = st.columns(3)

c1.metric("Total Tasks", total)
c2.metric("Completed", completed_count)
c3.metric("Pending", pending)

if total > 0:
    st.progress(completed_count / total)

st.divider()

# Task List
st.header("📋 Task List")

if tasks:
    df = pd.DataFrame(tasks)
    st.dataframe(
        df,
        use_container_width=True
    )
else:
    st.info("No Tasks Available")

# Expand View
with st.expander("View Task Details"):

    for i, t in enumerate(tasks):
        st.write(f"### {i+1}. {t['Task']}")
        st.write("Description:", t["Description"])
        st.write("Priority:", t["Priority"])
        st.write("Category:", t["Category"])
        st.write("Due:", t["Due Date"])
        st.write("Completed:", t["Completed"])
        st.divider()

# Delete Task
st.header("🗑 Delete Task")

if st.session_state.tasks:
    delete = st.selectbox(
        "Select Task",
        range(len(st.session_state.tasks)),
        format_func=lambda x:
        st.session_state.tasks[x]["Task"]
    )

    if st.button("Delete Selected"):
        st.session_state.tasks.pop(delete)
        st.success("Task Deleted")
        st.rerun()

# Download JSON
json_data = json.dumps(
    st.session_state.tasks,
    indent=4
)

st.download_button(
    "⬇ Download Tasks",
    json_data,
    "tasks.json",
    "application/json"
)

# Upload JSON
uploaded = st.file_uploader(
    "Upload Task File",
    type="json"
)

if uploaded:
    data = json.load(uploaded)
    st.session_state.tasks = data
    st.success("Tasks Imported Successfully!")

# Clear All
if st.button("❌ Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All Tasks Removed")
    st.rerun()