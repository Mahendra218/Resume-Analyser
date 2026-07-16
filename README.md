 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Python, Streamlit, Scikit-learn, and OpenRouter AI** that analyzes resumes, predicts job categories, calculates ATS scores, matches resumes with job descriptions, detects missing skills, generates AI feedback, interview questions, and downloadable PDF reports.


 Features

- Upload Resume (PDF)
- Resume Category Prediction using Machine Learning
- ATS Score Calculation
- Skill Extraction
- Resume vs Job Description Match
- Missing Skills Detection
- AI Resume Feedback (OpenRouter AI)
- AI Interview Question Generator
- Download Resume Analysis Report (PDF)



 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib
- PyMuPDF (fitz)
- ReportLab
- OpenRouter API
- dotenv

 Project Structure


AI-Resume-Analyzer/

app.py
train_model.py
requirements.txt
README.md
.env.example
model/
   clf.pkl
   tfidf.pkl

 Resume/
   Resume.csv

utils/
   ai.py
   ats.py
   interview.py
   jd_match.py
   missing_skills.py
   report.py
   skills.py


