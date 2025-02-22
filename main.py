from fastapi import FastAPI, HTTPException
import logging
from schemas import WebhookPayload
from firefly import get_firefly_transaction, get_firefly_attachments, update_firefly_transaction
from veryfi import send_to_veryfi

app = FastAPI()

@app.post("/webhook")
async def webhook_listener(payload: WebhookPayload):
    transaction_id = payload.content.id
    logging.info(f"Processing transaction ID: {transaction_id}")

    transaction = get_firefly_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    attachments = get_firefly_attachments(transaction_id)
    if not attachments:
        raise HTTPException(status_code=404, detail="No attachments found")

    veryfi_data = send_to_veryfi(attachments[0])
    if not veryfi_data:
        raise HTTPException(status_code=500, detail="Failed to process file with VeryFi")

    update_firefly_transaction(transaction_id, veryfi_data.get("ocr_text", "Updated via VeryFi"), veryfi_data.get("category", "Uncategorized"), [veryfi_data.get("name", "Receipt")])
    
    return {"message": "Transaction updated successfully"}
