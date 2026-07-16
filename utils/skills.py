import re

# Skills Database
SKILLS = [
    # Programming
    "Python", "C++", "C", "Java", "JavaScript", "SQL",

    # Web
    "HTML", "CSS", "React", "Node.js", "Express",

    # AI / ML
    "Machine Learning", "Deep Learning",
    "TensorFlow", "PyTorch", "Scikit-learn",
    "Pandas", "NumPy",

    # Cloud
    "AWS", "Azure", "GCP", "Docker", "Kubernetes",

    # Mechanical
    "SolidWorks", "AutoCAD", "CATIA",
    "ANSYS", "MATLAB",

    # Database
    "MongoDB", "MySQL", "PostgreSQL",

    # Tools
    "Git", "GitHub", "Linux"
]


def extract_skills(text):
    found = []

    text = text.lower()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    return sorted(list(set(found)))