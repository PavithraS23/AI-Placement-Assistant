import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Quiz Generator", layout="wide")

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

Generate a quiz based on the following details:

Topic: {topic}
Difficulty: {difficulty}
Number of Questions: {number}
Question Type: {quiz_type}

Rules:
- Use clear and simple language.
- Number each question properly.
- If MCQ, give 4 options.
- Mention the correct answer.
- Give a short explanation for each answer.
- Make it suitable for placement preparation.
"""

        with st.spinner("Generating quiz..."):
            response = llm.invoke(prompt)

        st.subheader("Generated Quiz")
        st.write(response.content)
