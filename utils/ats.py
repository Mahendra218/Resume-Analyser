import re

def calculate_ats_score(text, skills):

    score = 0
    feedback = []

    # Email
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
        score += 10
    else:
        feedback.append("Add a professional email address.")

    # Phone
    if re.search(r"\b\d{10}\b", text):
        score += 10
    else:
        feedback.append("Add a valid phone number.")

    # Skills
    if len(skills) >= 10:
        score += 30
    elif len(skills) >= 5:
        score += 20
    elif len(skills) >= 1:
        score += 10
    else:
        feedback.append("Add more technical skills.")

    # Education
    education_keywords = [
        "b.tech", "btech", "m.tech", "mtech",
        "b.e", "be", "degree", "engineering"
    ]

    if any(word in text.lower() for word in education_keywords):
        score += 20
    else:
        feedback.append("Mention your education clearly.")

    # Projects
    project_keywords = [
        "project", "projects", "developed",
        "built", "designed", "implemented"
    ]

    if any(word in text.lower() for word in project_keywords):
        score += 20
    else:
        feedback.append("Add academic or personal projects.")

    # Experience
    experience_keywords = [
        "experience", "internship", "intern",
        "worked", "company"
    ]

    if any(word in text.lower() for word in experience_keywords):
        score += 10
    else:
        feedback.append("Mention internship or experience if available.")

    return score, feedback