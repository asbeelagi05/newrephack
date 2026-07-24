import json
import os

from copilot import ClinicalCopilot
from report_generator import ReportGenerator
from speech.recorder import record_audio
from speech.transcriber import transcribe


def main():

    print("=" * 60)
    print("🏥 AI CLINICAL COPILOT")
    print("=" * 60)

    # -----------------------------
    # Step 1 : Record Consultation
    # -----------------------------
    record_audio("temp_audio.wav")

    # -----------------------------
    # Step 2 : Speech to Text
    # -----------------------------
    print("\n📝 Transcribing...\n")

    conversation = transcribe("temp_audio.wav")

    print("=" * 60)
    print("TRANSCRIPT")
    print("=" * 60)
    print(conversation)
    print("=" * 60)

    # -----------------------------
    # Step 3 : AI Analysis
    # -----------------------------
    
    print("\n🤖 Analyzing with Gemini...\n")

    copilot = ClinicalCopilot()
    result = copilot.analyze(conversation)

    # -----------------------------
    # Step 4 : Save JSON
    # -----------------------------
    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/extracted.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(result, file, indent=4)

    # -----------------------------
    # Step 5 : Generate Reports
    # -----------------------------
    report_generator = ReportGenerator()

    report = report_generator.generate(result)

    with open(
        "outputs/clinical_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    report_generator.generate_pdf(
        result,
        "outputs/clinical_report.pdf"
    )

    # -----------------------------
    # Step 6 : Print Results
    # -----------------------------
    print("\n")
    print(report)

    print("\nJSON Output:\n")
    print(json.dumps(result, indent=4))

    print("\n✅ Analysis Complete")
    print("📄 Text Report : outputs/clinical_report.txt")
    print("📑 PDF Report  : outputs/clinical_report.pdf")


if __name__ == "__main__":
    main()