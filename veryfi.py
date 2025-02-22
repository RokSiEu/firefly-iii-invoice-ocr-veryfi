import base64
import requests
import logging
from config import VERYFI_HOST, HEADERS_VERYFI

def send_to_veryfi(file_content):
    file_base64 = base64.b64encode(file_content).decode("utf-8")
    url = f"{VERYFI_HOST.rstrip('/')}/documents/"
    payload = {"file_data": file_base64, "file_name": "receipt.jpg", "auto_delete": True}
    try:
        response = requests.post(url, json=payload, headers=HEADERS_VERYFI)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error sending file to VeryFi: {e}")
        return None
