from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6JbKrEGkeYH2CMtLq1GkBP3SCfAyRWbuBjSxjGstJZjCQ"
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello!"
)

print(response.text)