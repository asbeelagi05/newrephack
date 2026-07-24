import json

from llm import ask_gemini
from prompts import MASTER_PROMPT


class ClinicalCopilot:

    def analyze(self, conversation: str) -> dict:

        prompt = MASTER_PROMPT.replace(
    "{conversation}",
    conversation
)

        response = ask_gemini(prompt)

        response = (
            response.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            return {
                "success": False,
                "error": "Invalid JSON returned by Gemini",
                "raw_response": response,
            }