import streamlit as st

st.title("Notes Chat")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

query = st.chat_input(
    "Ask a question..."
)
