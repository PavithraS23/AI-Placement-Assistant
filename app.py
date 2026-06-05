import streamlit as st

st.set_page_config(page_title="AI Placement Assistant", layout="wide")

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #1a102b 0%, #050505 45%, #000000 100%);
}

[data-testid="stSidebar"] {
    display: none;
}

.main-title {
    text-align: center;
    color: white;
    font-size: 58px;
    font-weight: 800;
    margin-top: 40px;
}

.main-title span {
    color: #a855f7;
}

.subtitle {
    text-align: center;
    color: #d1d5db;
    font-size: 18px;
    margin-bottom: 45px;
}

.start-title {
    text-align: center;
    color: #a855f7;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 25px;
}

.stButton > button {
    height: 150px;
    width: 100%;
    background-color: rgba(20, 20, 30, 0.95);
    color: white;
    border: 1px solid #a855f7;
    border-radius: 18px;
    font-size: 24px;
    font-weight: 700;
    box-shadow: 0 0 18px rgba(168, 85, 247, 0.25);
}

.stButton > button:hover {
    background-color: #1f1033;
    border: 1px solid #c084fc;
    color: #c084fc;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='main-title'>AI Placement <span>Assistant</span></div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Your AI-powered assistant for placement preparation, resume improvement, document learning and interview practice.</div>",
    unsafe_allow_html=True
)

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
