from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Sending request...")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Reply with only the word OK."
)

print(response.text)