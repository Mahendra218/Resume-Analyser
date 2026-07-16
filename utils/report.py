from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
    filename,
    prediction,
    score,
    skills,
    ai_feedback,
    match_score=None,
    missing_skills=None
):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Predicted Job:</b> {prediction}", styles["BodyText"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {score}/100", styles["BodyText"]))

    story.append(Paragraph(
        f"<b>Detected Skills:</b> {', '.join(skills)}",
        styles["BodyText"]
    ))

    if match_score is not None:
        story.append(Paragraph(
            f"<b>Resume Match:</b> {match_score}%",
            styles["BodyText"]
        ))

    if missing_skills:
        story.append(Paragraph(
            f"<b>Missing Skills:</b> {', '.join(missing_skills)}",
            styles["BodyText"]
        ))

    story.append(Paragraph("<b>AI Suggestions</b>", styles["Heading2"]))
    story.append(Paragraph(ai_feedback.replace("\n","<br/>"), styles["BodyText"]))

    doc.build(story)