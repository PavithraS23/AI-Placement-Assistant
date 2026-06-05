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
import os
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Mock Interview", layout="wide")

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
</style>
""", unsafe_allow_html=True)

st.title("Mock Interview")

if st.button("Back to Home"):
    st.switch_page("app.py")

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4
)

role = st.selectbox(
    "Select role",
    [
        "AI Engineer",
        "Data Analyst",
        "Java Developer",
        "Software Developer",
        "Machine Learning Intern"
    ]
)

level = st.selectbox(
    "Select level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Generate Interview Questions"):
    prompt = f"""
Generate 10 mock interview questions for the role: {role}

Candidate level: {level}

Include:
1. Technical questions
2. HR questions
3. Project-based questions
4. Short ideal answer for each question
"""

    with st.spinner("Preparing interview questions..."):
        response = llm.invoke(prompt)

    st.subheader("Interview Questions")
    st.write(response.content)
