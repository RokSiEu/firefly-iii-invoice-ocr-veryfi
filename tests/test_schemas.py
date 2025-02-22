import pytest
from schemas import WebhookPayload, Content, Transaction

def test_transaction_model():
    transaction = Transaction(
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
    )
    assert transaction.transaction_journal_id == "123"
    assert transaction.amount == "100.00"

def test_webhook_payload_model():
    payload = WebhookPayload(
        uuid="test-uuid",
        user_id=1,
        trigger="test-trigger",
        response="test-response",
        url="test-url",
        version="1.0",
        content=Content(
            id=123,
            transactions=[]
        )
    )
    assert payload.uuid == "test-uuid"
    assert payload.content.id == 123
