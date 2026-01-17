from fastapi import HTTPException
from services.currencycloud.client import get_auth_token


def currencycloud_token() -> str:
    try:
        return get_auth_token()
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Currencycloud authentication failed",
        )
