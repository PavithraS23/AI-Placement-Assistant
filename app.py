import streamlit as st

st.set_page_config(page_title="AI Placement Assistant", layout="wide")

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #171021 0%, #050505 45%, #000000 100%);
}

[data-testid="stSidebar"] {
    display: none;
}

.block-container {
    max-width: 980px;
    margin: auto;
    padding-top: 70px;
}

.main-title {
    text-align: center;
    font-size: 56px;
    font-weight: 800;
    color: white;
    margin-bottom: 14px;
}

.main-title span {
    color: #a855f7;
}

.subtitle {
    text-align: center;
    color: #d1d5db;
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 60px;
}

.start-title {
    text-align: center;
    color: #a855f7;
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 35px;
}

.stButton > button {
    height: 190px;
    width: 100%;
    background-color: rgba(18, 18, 28, 0.98);
    color: white;
    border: 1px solid #a855f7;
    border-radius: 22px;
    font-size: 24px;
    font-weight: 700;
    box-shadow: 0 0 22px rgba(168, 85, 247, 0.18);
}

.stButton > button:hover {
    background-color: #211033;
    color: #c084fc;
    border-color: #c084fc;
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

st.markdown(
    "<div class='start-title'>Let's Get Started</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

with col1:
    if st.button("Notes Chat", use_container_width=True):
        st.switch_page("pages/1_Notes_Chat.py")

with col2:
    if st.button("Quiz Generator", use_container_width=True):
        st.switch_page("pages/2_Quiz_Generator.py")

st.write("")

col3, col4 = st.columns(2, gap="large")

with col3:
    if st.button("Resume Analyzer", use_container_width=True):
        st.switch_page("pages/3_Resume_Analyzer.py")

with col4:
    if st.button("Mock Interview", use_container_width=True):
        st.switch_page("pages/4_Mock_Interview.py")
