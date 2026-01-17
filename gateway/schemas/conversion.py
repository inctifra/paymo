from pydantic import BaseModel, Field
from typing import List, Optional


class CreateConversionRequest(BaseModel):
    buy_currency: str = Field(..., description="Currency to buy, e.g., EUR")
    sell_currency: str = Field(..., description="Currency to sell, e.g., GBP")
    amount: float = Field(..., description="Amount to convert")
    fixed_side: str = Field("buy", description="Which side is fixed: 'buy' or 'sell'")
    reason: str = Field(
        ..., description="Reason for conversion, e.g., 'Top up balance'"
    )
    term_agreement: bool = Field(..., description="User must agree to terms, set true")


class CreateConversionResponse(BaseModel):
    id: str
    settlement_date: str
    conversion_date: str
    short_reference: str
    creator_contact_id: str
    account_id: str
    currency_pair: str
    status: str
    buy_currency: str
    sell_currency: str
    client_buy_amount: str
    client_sell_amount: str
    fixed_side: str
    core_rate: str
    partner_rate: Optional[str] = None
    partner_status: Optional[str] = None
    partner_buy_amount: Optional[str] = None
    partner_sell_amount: Optional[str] = None
    client_rate: str
    deposit_required: bool
    deposit_amount: str
    deposit_currency: Optional[str] = None
    deposit_status: Optional[str] = None
    deposit_required_at: Optional[str] = None
    payment_ids: List[str]
    unallocated_funds: str
    unique_request_id: Optional[str] = None
    created_at: str
    updated_at: str
    mid_market_rate: str
