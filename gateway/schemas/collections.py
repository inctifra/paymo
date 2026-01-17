from pydantic import BaseModel, Field
from typing import List, Optional

class FundingAccount(BaseModel):
    id: str
    account_id: str
    account_number: Optional[str]
    account_number_type: Optional[str]
    account_holder_name: Optional[str]
    bank_name: Optional[str]
    bank_address: Optional[str]
    bank_country: Optional[str]
    currency: str
    payment_type: str
    routing_code: Optional[str]
    routing_code_type: Optional[str]
    created_at: str
    updated_at: str

class Pagination(BaseModel):
    total_entries: int
    total_pages: int
    current_page: int
    per_page: int
    previous_page: int
    next_page: int
    order: str
    order_asc_desc: str

class FundingAccountsResponse(BaseModel):
    funding_accounts: List[FundingAccount]
    pagination: Pagination

# Push Notification Body
class PushNotificationHeader(BaseModel):
    message_type: str
    notification_type: str

class PushNotificationBody(BaseModel):
    id: str
    balance_id: str
    account_id: str
    currency: str
    amount: str
    balance_amount: Optional[str]
    type: str
    related_entity_type: str
    related_entity_id: str
    related_entity_short_reference: str
    status: str
    reason: Optional[str]
    settles_at: Optional[str]
    created_at: str
    updated_at: str
    completed_at: Optional[str]
    action: str

class PushNotification(BaseModel):
    header: PushNotificationHeader
    body: PushNotificationBody

# Accept/Reject Request
class CollectionScreeningRequest(BaseModel):
    accepted: bool = Field(..., description="True to accept, False to reject")
    reason: str = Field(..., description="Reason for accepting/rejecting")
    
# Accept/Reject Response
class CollectionScreeningResponse(BaseModel):
    transaction_id: str
    account_id: str
    house_account_id: str
    result: dict
