from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from enums.index import FundingAction


class FundingRequest(BaseModel):
    id: UUID = Field(..., description="Client-generated UUID for idempotency")

    receiver_account_number: str
    amount: float
    currency: str = Field(..., min_length=3, max_length=3)

    # Optional sender details
    sender_name: Optional[str] = None
    sender_address: Optional[str] = None
    sender_country: Optional[str] = Field(None, min_length=2, max_length=2)
    sender_reference: Optional[str] = None
    sender_account_number: Optional[str] = None
    sender_routing_code: Optional[str] = None

    receiver_routing_code: Optional[str] = None

    action: Optional[FundingAction] = FundingAction.approve
    on_behalf_of: Optional[UUID] = None


class FundingResponse(BaseModel):
    id: str
    account_id: str
    state: str

    sender_name: Optional[str]
    sender_address: Optional[str]
    sender_country: Optional[str]
    sender_reference: Optional[str]
    sender_account_number: Optional[str]
    sender_routing_code: Optional[str]

    receiver_account_number: str
    receiver_routing_code: Optional[str]

    amount: str
    currency: str
    action: str
    short_reference: str

    created_at: str
    updated_at: str
