import streamlit as st

st.set_page_config(page_title="AI Placement Assistant", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #000000;
}

[data-testid="stSidebar"] {
    display: none;
}

.main-title {
    text-align: center;
    color: #22c55e;
    font-size: 54px;
    font-weight: 800;
    margin-top: 60px;
}

.subtitle {
    text-align: center;
    color: #86efac;
    font-size: 18px;
    margin-bottom: 50px;
}

.start-title {
    text-align: center;
    color: #22c55e;
    font-size: 26px;
    margin-bottom: 25px;
}

.stButton > button {
    height: 120px;
    width: 100%;
    background-color: #0a0a0a;
    color: #22c55e;
    border: 1px solid #22c55e;
    border-radius: 14px;
    font-size: 22px;
    font-weight: 700;
}

.stButton > button:hover {
    background-color: #052e16;
    color: white;
    border-color: #22c55e;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>AI Placement Assistant</div>", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Your AI-powered assistant for placement preparation, resume improvement, document learning and interview practice.
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='start-title'>Let's Get Started</div>", unsafe_allow_html=True)

left, center, right = st.columns([1, 4, 1])

with center:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Notes Chat"):
            st.switch_page("pages/1_Notes_Chat.py")

    with col2:
        if st.button("Quiz Generator"):
            st.switch_page("pages/2_Quiz_Generator.py")

    col3, col4 = st.columns(2)

    with col3:
        if st.button("Resume Analyzer"):
            st.switch_page("pages/3_Resume_Analyzer.py")

    with col4:
        if st.button("Mock Interview"):
            st.switch_page("pages/4_Mock_Interview.py")
