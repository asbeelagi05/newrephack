from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


class ReportGenerator:

    def generate(self, data: dict) -> str:

        patient = data.get("patient", {})
        triage = data.get("triage", {})
        risk = data.get("risk_assessment", {})
        metadata = data.get("metadata", {})

        report = f"""
AI CLINICAL COPILOT REPORT

Generated:
{datetime.now().strftime("%d-%m-%Y %H:%M")}

==================================================

PATIENT INFORMATION

Chief Complaint:
{patient.get("chief_complaint","")}

History:
{patient.get("history_of_present_illness","")}

Symptoms:
{self.bullets(patient.get("symptoms",[]))}

Duration:
{patient.get("duration","")}

Severity:
{patient.get("severity","")}

Allergies:
{self.bullets(patient.get("allergies",[]))}

Current Medications:
{self.bullets(patient.get("current_medications",[]))}

==================================================

CLINICAL SUMMARY

{data.get("clinical_summary","")}

==================================================

TRIAGE

Urgency:
{triage.get("urgency","")}

Department:
{triage.get("department","")}

Wait Time:
{triage.get("estimated_wait_time","")}

==================================================

RISK ASSESSMENT

Risk Level:
{risk.get("risk_level","")}

Risk Score:
{risk.get("score","")}/100

Reason:
{risk.get("reason","")}

==================================================

RECOMMENDED TESTS

{self.bullets(data.get("recommended_tests",[]))}

==================================================

POSSIBLE CONDITIONS

{self.bullets(data.get("possible_conditions",[]))}

==================================================

FOLLOW UP QUESTIONS

{self.bullets(data.get("follow_up_questions",[]))}

==================================================

MISSING INFORMATION

{self.bullets(data.get("missing_information",[]))}

==================================================

DOCTOR HANDOFF

{data.get("doctor_handoff","")}

==================================================

PATIENT ADVICE

{self.bullets(data.get("patient_advice",[]))}

==================================================

AI CONFIDENCE

{metadata.get("model_confidence","")}

==================================================

DISCLAIMER

{metadata.get("disclaimer","")}
"""

        return report

    def generate_pdf(self, data, output_path):

        report = self.generate(data)

        doc = SimpleDocTemplate(output_path)

        styles = getSampleStyleSheet()

        story = []

        for line in report.split("\n"):

            if line.strip() == "":
                story.append(Spacer(1, 8))
            else:
                story.append(Paragraph(line, styles["BodyText"]))

        doc.build(story)

    @staticmethod
    def bullets(items):

        if not items:
            return "Not Available"

        return "<br/>".join([f"• {i}" for i in items])