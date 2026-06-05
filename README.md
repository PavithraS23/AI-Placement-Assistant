# AI Placement Assistant

AI Placement Assistant is a Generative AI-powered web application designed to help students prepare for placements through intelligent learning, resume analysis, quiz generation, and mock interview practice.

Built using Streamlit, Google Gemini, LangChain, and Python, the platform provides an interactive environment for placement preparation and career development.

---

## Features

### Notes Chat
- Upload PDF notes and study materials
- Ask questions from uploaded documents
- Generate summaries and explanations
- AI-powered document interaction

### Quiz Generator
- Generate Multiple Choice Questions (MCQs)
- Generate Aptitude Questions
- Generate Technical Interview Questions
- Select difficulty levels
- Download generated quizzes

### Resume Analyzer
- ATS Score Evaluation
- Technical Skill Assessment
- Placement Readiness Score
- Skill Gap Analysis
- Resume Improvement Suggestions
- Recommended Projects and Career Roles
- Resume-based Interview Questions

### Mock Interview
- Role-based Interview Questions
- AI-generated Feedback
- Answer Evaluation and Scoring
- Improvement Suggestions
- Personalized Interview Preparation

---

## Tech Stack

### Frontend
- Streamlit

### AI & NLP
- Google Gemini API
- LangChain

### Document Processing
- PyPDF

### Programming Language
- Python

### Deployment
- Streamlit Community Cloud

---

## Project Structure

```text
AI-Placement-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Notes_Chat.py
│   ├── 2_Quiz_Generator.py
│   ├── 3_Resume_Analyzer.py
│   └── 4_Mock_Interview.py
│
└── notebooks/
    └── AI_Placement_Assistant_Development.ipynb
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Placement-Assistant.git

cd AI-Placement-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API Key

Create a `.streamlit/secrets.toml` file:

```toml
GOOGLE_API_KEY = "YOUR_API_KEY"
```

Or add the API key through Streamlit Cloud Secrets during deployment.

---

## Run the Application

```bash
streamlit run app.py
```

---

## Sample Use Cases

### Notes Chat

```text
Summarize this PDF

Explain Retrieval Augmented Generation

Generate a 16-mark answer from the uploaded notes
```

### Quiz Generator

```text
Topic: Machine Learning

Difficulty: Medium

Question Type: MCQ
```

### Resume Analyzer

```text
Upload Resume

Get ATS Score
Identify Skill Gaps
Receive Project Recommendations
```

### Mock Interview

```text
Role: Data Analyst

Level: Intermediate

Generate Question
Submit Answer
Receive AI Feedback
```

---

## Future Enhancements

- Vector Database Integration (ChromaDB / FAISS)
- Retrieval-Augmented Generation (RAG)
- Voice-based Mock Interviews
- Learning Progress Tracking
- Personalized Learning Roadmaps
- User Authentication
- Multi-PDF Knowledge Base

---

## Learning Outcomes

- Generative AI Application Development
- Prompt Engineering
- LLM Integration
- Streamlit Application Development
- AI-powered Resume Analysis
- Intelligent Interview Preparation Systems
- Document Question Answering

---

## Author

**Pavithra Senthilkumaran**

B.Tech – Artificial Intelligence and Data Science  
Rajalakshmi Engineering College

