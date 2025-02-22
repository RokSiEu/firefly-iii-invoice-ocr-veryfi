import pytest
import requests
from unittest.mock import patch
from firefly import get_firefly_transaction, get_firefly_attachments, update_firefly_transaction


def test_get_firefly_transaction():
    transaction_id = 123
    mock_response = {"data": {"id": transaction_id, "attributes": {"description": "Test Transaction"}}}

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.raise_for_status = lambda: None
        response = get_firefly_transaction(transaction_id)
        assert response == mock_response


def test_get_firefly_attachments():
    transaction_id = 123
    mock_response = {"data": [{"id": "1", "attributes": {"filename": "receipt.jpg"}}]}

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.raise_for_status = lambda: None
        response = get_firefly_attachments(transaction_id)
        assert response == mock_response["data"]


def test_update_firefly_transaction():
    transaction_id = 123
    description = "Updated Description"
    category_name = "Updated Category"
    tags = ["Updated Tag"]
    mock_response = {"message": "Transaction updated"}

    with patch("requests.put") as mock_put:
        mock_put.return_value.json.return_value = mock_response
        mock_put.return_value.raise_for_status = lambda: None
        response = update_firefly_transaction(transaction_id, description, category_name, tags)
        assert response == mock_response
