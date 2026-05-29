import requests
from app.config import settings

def send_welcome_message(phone, customer_name):

    url = (
        f"{settings.WATI_API_URL}"
        "/api/ext/v3/messageTemplates/send"
    )

    headers = {
        "Authorization":
        f"Bearer {settings.WATI_API_KEY}",
        "Content-Type":
        "application/json"
    }

    payload = {
        "channel": "Default",
        "template_name": "welcome_message",
        "broadcast_name": "CRM Welcome",
        "recipients": [
            {
                "phone_number": phone,
                "custom_params": [
                    {
                        "name": "name",
                        "value": "Suji"
                    }
                ]
            }
        ]
    }

    print("URL =", url)
    print("HEADERS =", headers)
    print("PAYLOAD =", payload)

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    return {
        "status_code": response.status_code,
        "response": response.text
    }

    return response.json()