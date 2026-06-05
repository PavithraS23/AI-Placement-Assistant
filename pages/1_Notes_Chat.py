import streamlit as st
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Notes Chat", layout="wide")

st.title("Notes Chat")

if st.button("Back to Home"):
    st.switch_page("app.py")

# Check secret
try:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
    st.success("API key loaded")
except Exception as e:
    st.error(f"API key error: {e}")

# Check Gemini
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )
    st.success("Gemini model loaded")
except Exception as e:
    st.error(f"Gemini loading error: {e}")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded")

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            pdf_path = temp_file.name

        st.write("Temporary file created")

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        st.success(f"PDF read successfully. Pages: {len(documents)}")

        pdf_text = "\n".join([doc.page_content for doc in documents])

        st.write("Extracted text length:", len(pdf_text))

        st.text_area("PDF Preview", pdf_text[:2000], height=250)

        query = st.text_input("Ask a question")

        if st.button("Get Answer"):
            if query.strip() == "":
                st.warning("Please enter a question")
            else:
                prompt = f"""
Use the PDF content below to answer.

PDF Content:
{pdf_text[:12000]}

Question:
{query}

Answer:
"""

                response = llm.invoke(prompt)

                st.subheader("Answer")
                st.write(response.content)

    except Exception as e:
        st.error(f"PDF processing error: {e}")
else:
    st.info("Upload a PDF first")
