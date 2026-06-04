# AI Placement Assistant

AI Placement Assistant is a Generative AI application designed to help students prepare for placements through document-based question answering, quiz generation, resume analysis, and AI-powered mock interviews.

## Features

### Notes Chat

* Upload study materials and PDFs
* Ask questions from uploaded documents
* Retrieval-Augmented Generation (RAG) based responses
* Context-aware answers using Gemini AI

### Quiz Generator

* Generate multiple-choice questions
* Choose difficulty levels
* Create practice tests instantly

### Resume Analyzer

* Analyze resumes
* Identify strengths and skill gaps
* Suggest improvements and career recommendations

### Mock Interview

* Role-based interview practice
* AI-generated technical and HR questions
* Interactive interview experience

---

## Technology Stack

### Frontend

* Streamlit

### Generative AI

* Gemini 2.5 Flash

### Framework

* LangChain

### Vector Database

* ChromaDB

### Embeddings

* Gemini Embeddings

### PDF Processing

* PyPDF

---

## Project Structure

AI-Placement-Assistant/

├── app.py

├── requirements.txt

├── README.md

├── pages/

│   ├── 1_Notes_Chat.py

│   ├── 2_Quiz_Generator.py

│   ├── 3_Resume_Analyzer.py

│   └── 4_Mock_Interview.py

---

## Installation

Clone the repository:

git clone <repository-url>

cd AI-Placement-Assistant

Install dependencies:

pip install -r requirements.txt

---

## Configure API Key

Create a .env file:

GOOGLE_API_KEY=YOUR_API_KEY

Or add the key through Streamlit Secrets during deployment.

---

## Run Application

streamlit run app.py

---

## Future Enhancements

* Placement Readiness Score
* ATS Resume Scoring
* Personalized Learning Roadmaps
* Interview Performance Evaluation
* Multi-PDF Knowledge Base
* Progress Tracking Dashboard

---

## Author

Pavithra Senthilkumaran

B.Tech Artificial Intelligence and Data Science

Rajalakshmi Engineering College
