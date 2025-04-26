import requests

ZAPUP_API_KEY = (
    "x8JtrnzH7W4sap8UvjZpFJ0vqpceqUesuA7wObv7"  # Replace with your actual ZapUp API key
)
ZAPUP_SEND_URL = "https://box.zapup.press/api/send"
ZAPUP_SEND_IMAGE_URL = "https://box.zapup.press/api/send/media"


def send_whatsapp_message(payload, sender_number, sender_name):
    sender_names_str = ", ".join(set(sender_name))
    payload["phone"] = f"+{sender_number}"
    payload["message"] = f"Hello {sender_names_str}, {payload['message']}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ZAPUP_API_KEY}",
    }

    requests.post(ZAPUP_SEND_URL, json=payload, headers=headers)
    return "success"


def send_whatsapp_image(payload, sender_number):
    payload["phone"] = f"+{sender_number}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ZAPUP_API_KEY}",
    }

    requests.post(ZAPUP_SEND_IMAGE_URL, json=payload, headers=headers)
    return "success"

def send_text_message(phone: str, message: str):
    payload = {
        "phone": phone,
        "message": message
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ZAPUP_API_KEY}"
    }

    response = requests.post(ZAPUP_SEND_URL, headers=headers, json=payload)
    print(f"📤 Sent to {phone} | Status: {response.status_code}")
    return response.json()