from pydantic import BaseModel, Field


class DetailedFXQuoteRequest(BaseModel):
    buy_currency: str = Field(..., description="Currency to buy, e.g., EUR")
    sell_currency: str = Field(..., description="Currency to sell, e.g., GBP")
    amount: float = Field(..., description="Amount to convert")
    fixed_side: str = Field("buy", description="Which side is fixed: 'buy' or 'sell'")


class DetailedFXQuoteResponse(BaseModel):
    settlement_cut_off_time: str
    currency_pair: str
    client_buy_currency: str
    client_sell_currency: str
    client_buy_amount: str
    client_sell_amount: str
    fixed_side: str
    client_rate: str
    partner_rate: str | None
    core_rate: str
    deposit_required: bool
    deposit_amount: str
    deposit_currency: str
    mid_market_rate: str
