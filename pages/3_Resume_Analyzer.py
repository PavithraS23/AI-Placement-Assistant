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

.block-container {
    max-width: 950px;
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

[data-testid="stFileUploader"] {
    background-color: #111111;
    border: 1px solid #a855f7;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("Resume Analyzer")

if st.button("Back to Home"):
    st.switch_page("app.py")

try:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
except Exception:
    st.error("Gemini API key is missing. Add GOOGLE_API_KEY in Streamlit Secrets.")
    st.stop()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

resume = st.file_uploader("Upload Resume PDF", type=["pdf"])

if resume:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(resume.read())
        resume_path = temp_file.name

    try:
        loader = PyPDFLoader(resume_path)
        documents = loader.load()

        resume_text = "\n".join(
            [doc.page_content for doc in documents]
        )

        if len(resume_text.strip()) == 0:
            st.error("Could not extract text from this PDF. Please upload a text-based resume PDF.")
            st.stop()

        st.success("Resume uploaded successfully.")

        if st.button("Analyze Resume"):
            limited_resume_text = resume_text[:8000]

            prompt = f"""
You are an expert placement and resume advisor.

Analyze this resume professionally.

Give the output in this exact format:

1. Profile Summary

2. Scores
- ATS Score out of 100
- Technical Skill Score out of 100
- Placement Readiness Score out of 100

3. Strengths

4. Weak Areas

5. Missing Skills for Placements

6. Suitable Job Roles

7. Recommended Projects

8. Resume Improvement Tips

9. Interview Questions Based on Resume

Resume:
{limited_resume_text}
"""

            try:
                with st.spinner("Analyzing resume..."):
                    response = llm.invoke(prompt)

                resume_analysis = response.content

                st.subheader("Resume Analysis")
                st.write(resume_analysis)

                st.download_button(
                    label="Download Resume Analysis",
                    data=resume_analysis,
                    file_name="resume_analysis.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error("Resume analysis failed. Please try again.")
                st.write(str(e))

    except Exception as e:
        st.error("Failed to read the resume PDF.")
        st.write(str(e))

else:
    st.info("Upload your resume PDF to begin analysis.")
