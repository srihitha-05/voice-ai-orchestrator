import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def evaluate_lead(transcript: str):

    prompt = f"""
You are an AI assistant evaluating a real estate lead qualification call.

Analyze the transcript carefully.

Rules:

- Return QUALIFIED if the customer clearly shows interest in buying, selling, or renting.
- Return NOT_INTERESTED if the customer clearly declines.
- Return FAILED if the call failed or there is no meaningful conversation.
- Return NEEDS_REVIEW if:
  - the transcript is too short,
  - the conversation is ambiguous,
  - you are less than 80% confident,
  - or the customer's intent cannot be determined.

Return ONLY one of these values:

QUALIFIED
NOT_INTERESTED
FAILED
NEEDS_REVIEW

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()