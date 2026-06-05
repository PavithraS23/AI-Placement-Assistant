import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Quiz Generator", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: white;
}

.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 45px;
}

h1, h2, h3, p, label {
    color: white;
}

.stButton > button {
    background-color: #11111b;
    color: white;
    border: 1px solid #a855f7;
    border-radius: 10px;
}

.stButton > button:hover {
    background-color: #211033;
    color: #c084fc;
}
</style>
""", unsafe_allow_html=True)

st.title("Quiz Generator")

if st.button("Back to Home"):
    st.switch_page("app.py")

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

topic = st.text_input("Enter topic")

difficulty = st.selectbox(
    "Select difficulty",
    ["Easy", "Medium", "Hard"]
)

number = st.slider(
    "Number of questions",
    5,
    20,
    10
)

quiz_type = st.selectbox(
    "Question type",
    [
        "Multiple Choice Questions",
        "Short Answer Questions",
        "Interview Questions",
        "Aptitude Questions"
    ]
)

if st.button("Generate Quiz"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        prompt = f"""
You are an AI Placement Preparation Assistant.

Generate a quiz.

Topic: {topic}
Difficulty: {difficulty}
Number of Questions: {number}
Question Type: {quiz_type}

Rules:
- Number each question.
- If MCQ, give 4 options.
- Give the correct answer.
- Give a short explanation.
- Make it suitable for placement preparation.
"""

        with st.spinner("Generating quiz..."):
            response = llm.invoke(prompt)

        st.subheader("Generated Quiz")
        st.write(response.content)
