import os
import logging

# Load environment variables
FIREFLY_HOST = os.getenv("FIREFLY_HOST")
FIREFLY_TOKEN = os.getenv("FIREFLY_TOKEN")
FIREFLY_ATTACH_CSV = os.getenv("FIREFLY_ATTACH_CSV", "false").lower() == "true"

VERYFI_CLIENT_ID = os.getenv("VERYFI_CLIENT_ID")
VERYFI_CLIENT_SECRET = os.getenv("VERYFI_CLIENT_SECRET")
VERYFI_USERNAME = os.getenv("VERYFI_USERNAME")
VERYFI_API_KEY = os.getenv("VERYFI_API_KEY")
VERYFI_HOST = os.getenv("VERYFI_HOST", "https://api.veryfi.com/api/v8")

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Headers
HEADERS_JSON = {
    "Authorization": f"Bearer {FIREFLY_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

HEADERS_PUT = {
    "Authorization": f"Bearer {FIREFLY_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/octet-stream"
}

HEADERS_VERYFI = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"apikey {VERYFI_USERNAME}:{VERYFI_API_KEY}",
    "Client-Id": VERYFI_CLIENT_ID
}
