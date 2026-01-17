import json
from typing import Literal
from fastapi import APIRouter, Body, Depends, HTTPException
import requests
from services.currencycloud.client import auth_headers, _base_url
from dependencies.currencycloud import currencycloud_token

from schemas.fx import DetailedFXQuoteRequest, DetailedFXQuoteResponse
from schemas.conversion import CreateConversionRequest, CreateConversionResponse
from schemas.collections import (
    FundingAccountsResponse,
    PushNotification,
    CollectionScreeningRequest,
    CollectionScreeningResponse,
)
from schemas.accounts import AccountResponse, CreateAccountRequest
from schemas.funding import FundingResponse, FundingRequest
from schemas.payments import CreatePaymentRequest


router = APIRouter(
    prefix="/internal/currencycloud",
)


@router.get("/balances")
def all_balances(token: str = Depends(currencycloud_token)):
    r = requests.get(
        f"{_base_url()}/v2/balances/find",
        headers=auth_headers(token),
    )
    r.raise_for_status()
    return r.json()


@router.post("/fx-exchange", response_model=DetailedFXQuoteResponse)
def detailed_fx_quote(
    payload: DetailedFXQuoteRequest, token: str = Depends(currencycloud_token)
):
    """
    Get a detailed FX quote from Currencycloud.
    """
    url = f"{_base_url()}/v2/rates/detailed"
    params = {
        "buy_currency": payload.buy_currency.upper(),
        "sell_currency": payload.sell_currency.upper(),
        "amount": f"{payload.amount:.2f}",
        "fixed_side": payload.fixed_side.lower(),
    }

    response = requests.get(url, headers=auth_headers(token), params=params)
    response.raise_for_status()
    return response.json()


@router.post("/create-conversion", response_model=CreateConversionResponse)
def create_conversion(
    payload: CreateConversionRequest, token: str = Depends(currencycloud_token)
):
    """
    Create a currency conversion on Currencycloud.
    """
    url = f"{_base_url()}/v2/conversions/create"

    # Currencycloud expects multipart/form-data
    data = {
        "buy_currency": payload.buy_currency.upper(),
        "sell_currency": payload.sell_currency.upper(),
        "amount": f"{payload.amount:.2f}",
        "fixed_side": payload.fixed_side.lower(),
        "reason": payload.reason,
        "term_agreement": str(payload.term_agreement).lower(),  # true/false string
    }

    try:
        response = requests.post(url, headers=auth_headers(token), data=data)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=str(e))
    return response.json()


PaymentType = Literal["regular", "priority"]


# Step 1: Find Funding Accounts
@router.get("/funding-accounts/find", response_model=FundingAccountsResponse)
def find_funding_accounts(
    currency: str,
    account_id: str | None = None,
    payment_type: PaymentType = "regular",
    token: str = Depends(currencycloud_token),
):
    """
    Funding account
    
    {
      "id": "c2ff3cf4-7090-4cc0-897e-4bb13747c172",
      "account_id": "8528c5f0-9369-478e-8046-6383d711b789",
      "account_number": "GB79TCCL12345636721928",
      "account_number_type": "iban",
      "account_holder_name": "paymo",
      "bank_name": "The Currency Cloud Limited",
      "bank_address": "12 Steward Street, The Steward Building, London, E1 6FQ, GB",
      "bank_country": "GB",
      "currency": "KES",
      "payment_type": "priority",
      "routing_code": "TCCLGB3L",
      "routing_code_type": "bic_swift",
      "created_at": "2026-01-14T04:59:58+00:00",
      "updated_at": "2026-01-14T04:59:58+00:00"
    }
    
    """
    url = f"{_base_url()}/v2/funding_accounts/find"
    params = {
        "payment_type": payment_type,
        "currency": currency,
        "account_id": account_id,
    }
    try:
        r = requests.get(url, headers=auth_headers(token), params=params)
        print(json.loads(r.content))
        r.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=str(e))
    return r.json()


# Step 2: Handle push notifications (POST webhook)
@router.post("/push-notification", response_model=PushNotification)
def receive_push_notification(payload: PushNotification = Body(...)):
    """
    Receive inbound funds push notifications from Currencycloud
    """
    # Here you can store the notification in DB or process it
    return payload


# Step 3: Accept or Reject inbound transaction
@router.post(
    "/screening/{transaction_id}/complete", response_model=CollectionScreeningResponse
)
def screening_transaction(
    transaction_id: str,
    payload: CollectionScreeningRequest,
    token: str = Depends(currencycloud_token),
):
    url = f"{_base_url()}/v2/collections_screening/{transaction_id}/complete"
    data = {
        "accepted": str(payload.accepted).lower(),  # true/false string
        "reason": payload.reason,
    }
    try:
        r = requests.post(url, headers=auth_headers(token), data=data)
        r.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=str(e))
    return r.json()


@router.post("/sub-accounts/create", response_model=AccountResponse)
def create_sub_account(
    payload: CreateAccountRequest, token: str = Depends(currencycloud_token)
):
    """
    Create a new Currencycloud sub-account.
    """
    url = f"{_base_url()}/v2/accounts/create"
    try:
        r = requests.post(
            url,
            headers=auth_headers(token),
            json=payload.model_dump(exclude_none=True),
        )
        r.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=str(e))

    return r.json()


@router.post(
    "/funding/create",
    response_model=FundingResponse,
)
def emulate_funding(
    payload: FundingRequest,
    token: str = Depends(currencycloud_token),
):
    """
    Emulate inbound funding (DEMO ONLY).
    """
    url = f"{_base_url()}/v2/demo/funding/create"

    try:
        r = requests.post(
            url,
            headers=auth_headers(token),
            data=payload.model_dump(exclude_none=True),
            timeout=10,
        )
        r.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=r.text if r else str(e))
    return r.json()


@router.get("/accounts/find")
def find_accounts(
    token: str = Depends(currencycloud_token),
):
    """
    Find accounts or this user.
    """
    url = f"{_base_url()}/v2/accounts/find"

    try:
        r = requests.post(
            url,
            headers=auth_headers(token),
            timeout=10,
        )
        print(json.loads(r.content))
        r.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=r.text if r else str(e))
    return r.json()


@router.post("/payments/create")
def create_payment(
    payload: CreatePaymentRequest,
    token: str = Depends(currencycloud_token),
):
    """
    Find accounts or this user.
    """
    url = f"{_base_url()}/v2/payments/create"

    try:
        r = requests.post(
            url,
            headers=auth_headers(token),
            json=payload.model_dump(),
            timeout=10,
        )
        print(json.loads(r.content))
        r.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=r.text if r else str(e))
    return r.json()
