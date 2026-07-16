import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def get_ai_feedback(resume_text):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze this resume.

Give:

1. Overall Review

2. Strengths

3. Weaknesses

4. Missing Sections

5. ATS Improvement Tips

6. Technical Skills Improvement

7. Final Score out of 10

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