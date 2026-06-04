import streamlit as st

st.title("Mock Interview")

role = st.selectbox(
    "Role",
    [
        "AI Engineer",
        "Data Analyst",
        "Java Developer"
    ]
)
