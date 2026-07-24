from dotenv import dotenv_values
from google import genai

# Read .env
config = dotenv_values(".env")

API_KEY = config["GEMINI_API_KEY"]
MODEL_NAME = "gemini-3.6-flash"

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt: str) -> str:
    print(f"Using model: {MODEL_NAME}")

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text