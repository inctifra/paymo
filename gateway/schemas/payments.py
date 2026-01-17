from pydantic import BaseModel, Field
from uuid import UUID


class CreatePaymentRequest(BaseModel):
    currency: str = Field(..., min_length=3, max_length=3)
    beneficiary_id: str
    amount: str = Field(..., pattern=r"^\d+(\.\d{1,2})?$")
    reason: str
    reference: str
    unique_request_id: str