import pytest
import requests
from unittest.mock import patch
from veryfi import send_to_veryfi


def test_send_to_veryfi():
    mock_response = {"id": "12345", "ocr_text": "Receipt Data"}
    file_content = b"test file data"

    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = mock_response
        mock_post.return_value.raise_for_status = lambda: None
        response = send_to_veryfi(file_content)
        assert response == mock_response
