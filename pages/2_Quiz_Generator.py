import streamlit as st

st.title("Quiz Generator")

topic = st.text_input("Topic")

difficulty = st.selectbox(
    "Difficulty",
    ["Easy","Medium","Hard"]
)
