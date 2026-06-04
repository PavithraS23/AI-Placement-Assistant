import streamlit as st

st.set_page_config(
    page_title="AI Placement Assistant",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color:#0b1220;
}

[data-testid="stSidebar"]{
    display:none;
}

h1,h2,h3,p{
    color:white;
}

.tool-card{
    background:#111827;
    border:1px solid #16a34a;
    border-radius:12px;
    padding:25px;
    text-align:center;
    margin-bottom:20px;
}

.tool-title{
    font-size:24px;
    font-weight:600;
    color:white;
}

.tool-desc{
    font-size:15px;
    color:#d1d5db;
}

.stButton > button{
    width:100%;
    height:120px;
    background-color:#111827;
    border:1px solid #16a34a;
    border-radius:12px;
    color:white;
    font-size:20px;
}

.stButton > button:hover{
    border-color:#22c55e;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<h1 style='text-align:center;'>
AI Placement Assistant
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p style='text-align:center;font-size:18px;'>
Your AI-powered companion for placement preparation,
career development and interview success.
</p>
""",
unsafe_allow_html=True
)

st.write("")
st.write("")

st.markdown(
"""
<h3 style='text-align:center;'>
Let's Get Started
</h3>
""",
unsafe_allow_html=True
)

st.write("")

left, center, right = st.columns([1,4,1])

with center:

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Notes Chat",
            use_container_width=True
        ):
            st.switch_page(
                "pages/1_Notes_Chat.py"
            )

    with col2:
        if st.button(
            "Quiz Generator",
            use_container_width=True
        ):
            st.switch_page(
                "pages/2_Quiz_Generator.py"
            )

    col3, col4 = st.columns(2)

    with col3:
        if st.button(
            "Resume Analyzer",
            use_container_width=True
        ):
            st.switch_page(
                "pages/3_Resume_Analyzer.py"
            )

    with col4:
        if st.button(
            "Mock Interview",
            use_container_width=True
        ):
            st.switch_page(
                "pages/4_Mock_Interview.py"
            )
