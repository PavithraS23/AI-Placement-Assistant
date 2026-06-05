st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #1a102b 0%, #050505 45%, #000000 100%);
    color: white;
}

h1, h2, h3, p, label {
    color: white;
}

.stButton > button {
    background-color: rgba(20, 20, 30, 0.95);
    color: white;
    border: 1px solid #a855f7;
    border-radius: 10px;
}

.stButton > button:hover {
    background-color: #1f1033;
    color: #c084fc;
    border-color: #c084fc;
}

.stTextInput input {
    background-color: #111111;
    color: white;
    border: 1px solid #a855f7;
}

[data-testid="stFileUploader"] {
    background-color: #111111;
    border: 1px solid #a855f7;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
import streamlit as st
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Resume Analyzer", layout="wide")

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

[data-testid="stFileUploader"] {
    background-color: #111111;
    border: 1px solid #22c55e;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("Resume Analyzer")

if st.button("Back to Home"):
    st.switch_page("app.py")

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

resume = st.file_uploader("Upload Resume PDF", type=["pdf"])

if resume:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(resume.read())
        resume_path = temp_file.name

    loader = PyPDFLoader(resume_path)
    documents = loader.load()

    resume_text = "\n".join(
        [doc.page_content for doc in documents]
    )

    if st.button("Analyze Resume"):
        prompt = f"""
You are an expert placement and resume advisor.

Analyze this resume.

Give:
1. Short profile summary
2. Strong skills
3. Weak areas
4. Missing skills for placements
5. Suitable job roles
6. Project suggestions
7. Resume improvement tips
8. Interview questions based on this resume

Resume:
{resume_text}
"""

        with st.spinner("Analyzing resume..."):
            response = llm.invoke(prompt)

        st.subheader("Resume Analysis")
        st.write(response.content)
