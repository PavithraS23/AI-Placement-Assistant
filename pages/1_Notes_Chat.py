import streamlit as st
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

st.set_page_config(page_title="Notes Chat", layout="wide")

st.title("Notes Chat")

if st.button("Back to Home"):
    st.switch_page("app.py")

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "llm" not in st.session_state:
    st.session_state.llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )

if uploaded_file and st.session_state.retriever is None:
    with st.spinner("Reading and processing PDF..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            pdf_path = temp_file.name

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        docs = splitter.split_documents(documents)

        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001"
        )

        vectorstore = Chroma.from_documents(
            documents=docs,
            embedding=embeddings
        )

        st.session_state.retriever = vectorstore.as_retriever()

    st.success("PDF processed successfully. You can ask questions now.")

if st.session_state.retriever:
    query = st.chat_input("Ask a question from your PDF")

    if query:
        st.chat_message("user").write(query)

        with st.spinner("Searching document and generating answer..."):
            docs_found = st.session_state.retriever.invoke(query)

            context = "\n\n".join(
                [doc.page_content for doc in docs_found[:4]]
            )

            prompt = f"""
You are an AI Placement Assistant.

Answer using only the context below.

If the answer is not available in the document, say:
"The uploaded document does not contain this information."

Context:
{context}

Question:
{query}

Answer:
"""

            response = st.session_state.llm.invoke(prompt)

        st.chat_message("assistant").write(response.content)

else:
    st.info("Upload a PDF first to start asking questions.")
