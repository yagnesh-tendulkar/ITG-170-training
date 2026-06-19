from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def create_interview_report(
    filename: str,
    candidate_name: str,
    role: str,
    question: str,
    response: str,
    technical_score: int,
    communication_score: int,
    feedback: str,
    suggestions: list[str],
) -> str:
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = {
        "title": ParagraphStyle(name="Title", fontSize=18, leading=22, spaceAfter=14),
        "heading": ParagraphStyle(name="Heading", fontSize=12, leading=14, spaceAfter=8),
        "body": ParagraphStyle(name="Body", fontSize=10, leading=14, spaceAfter=8),
    }

    elements = [
        Paragraph("Interview Report", styles["title"]),
        Paragraph(f"Candidate Name: {candidate_name}", styles["body"]),
        Paragraph(f"Role: {role}", styles["body"]),
        Spacer(1, 12),
        Paragraph("Scores:", styles["heading"]),
        Paragraph(f"Technical Score: {technical_score}", styles["body"]),
        Paragraph(f"Communication Score: {communication_score}", styles["body"]),
        Spacer(1, 12),
        Paragraph("Question:", styles["heading"]),
        Paragraph(question, styles["body"]),
        Spacer(1, 12),
        Paragraph("Candidate Response:", styles["heading"]),
        Paragraph(response, styles["body"]),
        Spacer(1, 12),
        Paragraph("Feedback:", styles["heading"]),
        Paragraph(feedback, styles["body"]),
        Spacer(1, 12),
        Paragraph("Improvement Suggestions:", styles["heading"]),
    ]

    for suggestion in suggestions:
        elements.append(Paragraph(f"• {suggestion}", styles["body"]))

    doc.build(elements)
    return filename
