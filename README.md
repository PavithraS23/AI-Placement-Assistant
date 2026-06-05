# AI Placement Assistant

An AI-powered placement preparation platform built using Streamlit and Google Gemini. The application helps students prepare for placements through document-based learning, quiz generation, resume analysis, and mock interview practice.

## Features

### Notes Chat
- Upload PDF documents
- Ask questions from notes and study materials
- Generate summaries and explanations
- AI-powered document interaction

### Quiz Generator
- Generate Multiple Choice Questions (MCQs)
- Generate Interview Questions
- Generate Aptitude Questions
- Select difficulty levels
- Download generated quizzes

### Resume Analyzer
- ATS Score Evaluation
- Technical Skill Assessment
- Placement Readiness Analysis
- Skill Gap Identification
- Resume Improvement Suggestions
- Recommended Projects and Roles

### Mock Interview
- Role-based interview questions
- AI-generated feedback
- Answer evaluation and scoring
- Personalized interview preparation

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- LangChain
- PyPDF

## Project Structure

```text
AI-Placement-Assistant
│
├── app.py
├── requirements.txt
│
└── pages
    ├── 1_Notes_Chat.py
    ├── 2_Quiz_Generator.py
    ├── 3_Resume_Analyzer.py
    └── 4_Mock_Interview.py
```

## Installation

```bash
git clone https://github.com/your-username/AI-Placement-Assistant.git

cd AI-Placement-Assistant

pip install -r requirements.txt
```

## Configure API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GOOGLE_API_KEY = "YOUR_API_KEY"
```

## Run Application

```bash
streamlit run app.py
```

## Future Enhancements

- Vector Database Integration
- RAG-based Question Answering
- Voice-based Interviews
- Progress Tracking Dashboard
- Learning Roadmaps
- User Authentication

## Author

**Pavithra Senthilkumaran**

B.Tech Artificial Intelligence and Data Science

Rajalakshmi Engineering College
