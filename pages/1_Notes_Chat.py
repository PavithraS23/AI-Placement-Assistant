import streamlit as st
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Notes Chat", layout="wide")

st.title("Notes Chat")

if st.button("Back to Home"):
    st.switch_page("app.py")

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

if uploaded_file and st.session_state.pdf_text == "":
    with st.spinner("Reading PDF..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            pdf_path = temp_file.name

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        st.session_state.pdf_text = "\n".join(
            [doc.page_content for doc in documents]
        )

    st.success("PDF processed successfully.")

if st.session_state.pdf_text:
    st.write("PDF is ready. Ask your question below.")

    query = st.text_input("Ask a question")

    if st.button("Get Answer"):
        if query.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Generating answer..."):
                prompt = f"""
You are an AI Placement Assistant.

Use only the PDF content below to answer.

PDF Content:
{st.session_state.pdf_text[:12000]}

Question:
{query}

Answer:
"""
                response = llm.invoke(prompt)

            st.subheader("Answer")
            st.write(response.content)
else:
    st.info("Upload a PDF first.")
