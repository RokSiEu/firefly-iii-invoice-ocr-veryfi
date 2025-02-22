import requests
import logging
from config import FIREFLY_HOST, HEADERS_JSON

def get_firefly_transaction(transaction_id):
    url = f"{FIREFLY_HOST}/api/v1/transactions/{transaction_id}"
    try:
        response = requests.get(url, headers=HEADERS_JSON)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching transaction: {e}")
        return None

def get_firefly_attachments(transaction_id):
    url = f"{FIREFLY_HOST}/api/v1/attachments?transaction_id={transaction_id}"
    try:
        response = requests.get(url, headers=HEADERS_JSON)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.RequestException as e:
        logging.error(f"Error fetching attachments: {e}")
        return None

def update_firefly_transaction(transaction_id, description, category_name, tags):
    url = f"{FIREFLY_HOST}/api/v1/transactions/{transaction_id}"
    transaction_data = {
        "apply_rules": False,
        "fire_webhooks": True,
        "transactions": [
            {
                "transaction_journal_id": str(transaction_id),
                "category_name": category_name,
                "tags": tags,
                "notes": description
            }
        ]
    }
    try:
        response = requests.put(url, json=transaction_data, headers=HEADERS_JSON)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error updating transaction: {e}")
        return None
