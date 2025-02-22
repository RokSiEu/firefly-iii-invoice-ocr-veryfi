from typing import List, Optional, Union
from pydantic import BaseModel, field_validator

class Transaction(BaseModel):
    transaction_journal_id: Union[str, int]
    type: str
    date: str  # ISO 8601 date format
    amount: str  # Ensure it's always a string
    description: Optional[str]
    order: Optional[int]
    currency_id: Union[str, int]
    currency_code: Optional[str]
    category_name: Optional[str]
    source_id: Union[str, int]
    source_name: Optional[str]
    destination_id: Union[str, int]
    destination_name: Optional[str]
    tags: Optional[List[str]]
    notes: Optional[str]

    @field_validator("transaction_journal_id", "currency_id", "source_id", "destination_id", mode="before")
    @classmethod
    def convert_int_to_str(cls, value):
        return str(value) if isinstance(value, int) else value

class Content(BaseModel):
    id: int
    transactions: List[Transaction]

class WebhookPayload(BaseModel):
    uuid: str
    user_id: int
    trigger: str
    response: str
    url: str
    version: str
    content: Content
