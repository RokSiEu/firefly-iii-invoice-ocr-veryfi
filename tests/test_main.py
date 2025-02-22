import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from schemas import WebhookPayload, Content, Transaction

client = TestClient(app)


def test_webhook_listener():
    payload = WebhookPayload(
        uuid="test-uuid",
        user_id=1,
        trigger="test-trigger",
        response="test-response",
        url="test-url",
        version="1.0",
        content=Content(
            id=123,
            transactions=[Transaction(
                transaction_journal_id="123",
                type="expense",
                date="2024-02-18",
                amount="100.00",
                description="Test transaction",
                order=None,
                currency_id="1",
                currency_code="USD",
                category_name="Test Category",
                source_id="1",
                source_name="Bank",
                destination_id="2",
                destination_name="Store",
                tags=["tag1"],
                notes="Test note"
            )]
        )
    )

    with patch("main.get_firefly_transaction", return_value={"data": {}}), \
            patch("main.get_firefly_attachments", return_value=["mock-url"]), \
            patch("main.send_to_veryfi",
                  return_value={"ocr_text": "Test Receipt", "category": "Food", "name": "Receipt"}), \
            patch("main.update_firefly_transaction", return_value={"message": "Transaction updated successfully"}):
        response = client.post("/webhook", json=payload.dict())
        assert response.status_code == 200
        assert response.json() == {"message": "Transaction updated successfully"}
