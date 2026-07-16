from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_interview_questions(resume_text):

    prompt = f"""
You are a Technical Interviewer.

Based on the following resume, generate:

1. 10 Technical Interview Questions
2. 5 HR Interview Questions
3. 5 Project-based Questions

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content