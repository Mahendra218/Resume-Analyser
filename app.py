import streamlit as st
import joblib
import fitz

from utils.skills import extract_skills
from utils.ats import calculate_ats_score
from utils.jd_match import calculate_match
from utils.missing_skills import compare_skills
from utils.ai import get_ai_feedback
from utils.report import generate_report
from utils.interview import generate_interview_questions

# Load ML Model
model = joblib.load("model/clf.pkl")
tfidf = joblib.load("model/tfidf.pkl")

# Page Config
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title(" AI Resume Analyzer")


uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


jd_file = st.file_uploader(
    "Upload Job Description (Optional)",
    type=["pdf", "txt"]
)

if uploaded_file is not None:

   
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    
    vector = tfidf.transform([text])
    prediction = model.predict(vector)[0]

    
    skills = extract_skills(text)

    
    score, ats_feedback = calculate_ats_score(text, skills)

    
    st.subheader("Predicted Job Category")
    st.success(prediction)

    st.subheader("Detected Skills")

    if skills:
        st.write(", ".join(skills))
    else:
        st.warning("No skills detected.")

    st.subheader("ATS Score")
    st.progress(score / 100)
    st.success(f"{score}/100")

    st.subheader("ATS Suggestions")

    if ats_feedback:
        for item in ats_feedback:
            st.write(f"• {item}")
    else:
        st.success("Excellent Resume!")

    
    st.subheader(" AI Resume Suggestions")

    if st.button("Analyze with AI"):

        with st.spinner("Analyzing Resume..."):

            ai_feedback = get_ai_feedback(text)

        st.write(ai_feedback)

       
        match_score = None
        missing = []


    st.subheader(" AI Interview Questions")

    if st.button("Generate Interview Questions"):

        with st.spinner("Generating Questions..."):

            interview_questions = generate_interview_questions(text)

        st.markdown(interview_questions)

      
        if jd_file is not None:

            if jd_file.name.endswith(".pdf"):

                pdf = fitz.open(
                    stream=jd_file.read(),
                    filetype="pdf"
                )

                jd_text = ""

                for page in pdf:
                    jd_text += page.get_text()

            else:

                jd_text = jd_file.read().decode("utf-8")

            match_score = calculate_match(text, jd_text)

            st.subheader("Resume vs Job Description Match")

            st.progress(match_score / 100)

            st.success(f"{match_score}% Match")

            matched, missing = compare_skills(text, jd_text)

            st.subheader("Matched Skills")

            if matched:
                for skill in matched:
                    st.success(f"{skill}")
            else:
                st.warning("No matching skills found.")

            st.subheader("Missing Skills")

            if missing:
                for skill in missing:
                    st.error(f" {skill}")
            else:
                st.success("No missing skills!")

        
        generate_report(
            filename="Resume_Report.pdf",
            prediction=prediction,
            score=score,
            skills=skills,
            ai_feedback=ai_feedback,
            match_score=match_score,
            missing_skills=missing
        )

        with open("Resume_Report.pdf", "rb") as pdf_file:

            st.download_button(
                label=" Download Report",
                data=pdf_file,
                file_name="Resume_Report.pdf",
                mime="application/pdf"
            )
