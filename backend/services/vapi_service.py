import os
import requests
from dotenv import load_dotenv

load_dotenv()

VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_ASSISTANT_ID = os.getenv("VAPI_ASSISTANT_ID")
PHONE_NUMBER_ID = os.getenv("VAPI_PHONE_NUMBER_ID")

def make_call(customer):

    url = "https://api.vapi.ai/call"

    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "assistantId": VAPI_ASSISTANT_ID,
        "phoneNumberId": PHONE_NUMBER_ID,
        "customer": {
            "number": customer["phone"]
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    return response