from pydantic import BaseModel, Field
from typing import Literal, Optional, List


class CreateAccountRequest(BaseModel):
    account_name: str
    legal_entity_type: Literal["company", "individual"]
    legal_entity_sub_type: Literal[
        "sole_trader",
        "limited_liability_company",
        "public_limited_company",
        "limited_liability_partnership",
        "unincorporated_partnership",
        "unregistered_charity",
        "registered_charity",
        "trust",
        "company_with_nominee_shareholders_or_shares_in_bearer_form",
        "scottish_limited_partnership",
        "other",
    ]
    street: str
    city: str
    country: str
    postal_code: str
    brand: str
    your_reference: str | None = None
    status: str = "enabled"
    spread_table: str = "flat_0.00"
    api_trading: bool = True
    online_trading: bool = True
    phone_trading: bool = True
    identification_type: str
    identification_value: str
    identification_issuer: str
    identification_expiration: str
    terms_and_conditions_accepted: bool
    industry_type: str
    business_website_url: str
    country_of_incorporation: str
    date_of_incorporation: str
    expected_monthly_activity_volume: int
    expected_monthly_activity_value: int
    # expected_transaction_currencies: List[str] = Field(..., max_items=1)
    # expected_transaction_countries: List[str] = Field(..., min_items=1)


class AccountResponse(BaseModel):
    id: str
    account_name: str
    brand: Optional[str]
    your_reference: Optional[str]
    status: str
    street: str
    city: str
    state_or_province: Optional[str]
    country: str
    postal_code: Optional[str]
    spread_table: Optional[str]
    legal_entity_type: str
    created_at: str
    updated_at: str
    identification_type: Optional[str]
    identification_value: Optional[str]
    identification_issuer: Optional[str]
    identification_expiration: Optional[str]
    short_reference: Optional[str]
    api_trading: bool
    online_trading: bool
    phone_trading: bool
    bank_account_verified: Optional[str]
