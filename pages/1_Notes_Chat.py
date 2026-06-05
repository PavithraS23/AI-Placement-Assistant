import streamlit as st
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Notes Chat", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: white;
}

h1, h2, h3, p, label {
    color: #22c55e;
}

.stButton > button {
    background-color: #0a0a0a;
    color: #22c55e;
    border: 1px solid #22c55e;
    border-radius: 10px;
}

.stButton > button:hover {
    background-color: #052e16;
    color: white;
}

.stTextInput input {
    background-color: #111111;
    color: white;
    border: 1px solid #22c55e;
}

[data-testid="stFileUploader"] {
    background-color: #111111;
    border: 1px solid #22c55e;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("Notes Chat")

if st.button("Back to Home"):
    st.switch_page("app.py")

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

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
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    query = st.chat_input("Ask a question from your PDF")

    if query:
        st.session_state.messages.append(
            {"role": "user", "content": query}
        )

        with st.chat_message("user"):
            st.write(query)

        prompt = f"""
You are an AI Placement Assistant.

Use only the PDF content below to answer.

PDF Content:
{st.session_state.pdf_text[:12000]}

Question:
{query}

Answer:
"""

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = llm.invoke(prompt)
                answer = response.content
                st.write(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

else:
    st.info("Upload a PDF first.")
