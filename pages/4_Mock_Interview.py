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

if "interview_question" not in st.session_state:
    st.session_state.interview_question = ""

if st.button("Generate Question"):
    prompt = f"""
Generate one interview question for the role: {role}

Candidate level: {level}

The question should be suitable for placement preparation.
Do not give answer.
"""

    with st.spinner("Generating question..."):
        response = llm.invoke(prompt)

    st.session_state.interview_question = response.content

if st.session_state.interview_question:
    st.subheader("Interview Question")
    st.write(st.session_state.interview_question)

    user_answer = st.text_area(
        "Type your answer here",
        height=180
    )

    if st.button("Evaluate My Answer"):
        if user_answer.strip() == "":
            st.warning("Please type your answer first.")
        else:
            feedback_prompt = f"""
You are an expert interview evaluator.

Role: {role}
Level: {level}

Interview Question:
{st.session_state.interview_question}

Candidate Answer:
{user_answer}

Evaluate the answer and give:

1. Score out of 10
2. Strengths in the answer
3. Mistakes or missing points
4. Improved ideal answer
5. Final interview tip
"""

            with st.spinner("Evaluating answer..."):
                feedback = llm.invoke(feedback_prompt)

            feedback_output = feedback.content

            st.subheader("Feedback")
            st.write(feedback_output)

            st.download_button(
                label="Download Feedback",
                data=feedback_output,
                file_name="interview_feedback.txt",
                mime="text/plain"
            )
