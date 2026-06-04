import streamlit as st

st.title("Resume Analyzer")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)
