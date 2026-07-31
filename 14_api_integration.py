import streamlit as st
import requests

st.set_page_config(
    page_title="API Integration",
    layout="wide"
)

st.title("🌐 REST API Explorer Dashboard")

BASE_URL = "https://jsonplaceholder.typicode.com"

menu = st.sidebar.radio(
    "Choose Operation",
    ["GET", "POST", "PUT", "DELETE"]
)

# GET 
if menu == "GET":
    st.header("📥 GET Users")

    if st.button("Fetch Users"):
        response = requests.get(f"{BASE_URL}/users", timeout=10)

        st.success(f"Status Code: {response.status_code}")

        users = response.json()

        for user in users:
            with st.expander(user["name"]):
                st.write(f"**Email:** {user['email']}")
                st.write(f"**Phone:** {user['phone']}")
                st.write(f"**Website:** {user['website']}")

# POST 
elif menu == "POST":
    st.header("➕ Create User")

    with st.form("post_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")

        submitted = st.form_submit_button("Create")

    if submitted:
        payload = {
            "name": name,
            "email": email
        }

        response = requests.post(
            f"{BASE_URL}/users",
            json=payload,
            timeout=10
        )

        st.success(f"Status Code: {response.status_code}")
        st.json(response.json())

#  PUT 
elif menu == "PUT":
    st.header("✏ Update User")

    user_id = st.number_input(
        "User ID",
        min_value=1,
        value=1
    )

    new_name = st.text_input("Updated Name")

    if st.button("Update User"):
        payload = {"name": new_name}

        response = requests.put(
            f"{BASE_URL}/users/{user_id}",
            json=payload,
            timeout=10
        )

        st.success(f"Status Code: {response.status_code}")
        st.json(response.json())

# DELETE 
elif menu == "DELETE":
    st.header("🗑 Delete User")

    user_id = st.number_input(
        "Delete User ID",
        min_value=1,
        value=1,
        key="delete_id"
    )

    if st.button("Delete User"):
        response = requests.delete(
            f"{BASE_URL}/users/{user_id}",
            timeout=10
        )

        st.success(f"Status Code: {response.status_code}")
        st.info("Delete request sent successfully.")

        if response.text:
            st.json(response.json())