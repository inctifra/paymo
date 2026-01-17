import time
import requests
from threading import Lock
from config.settings.base import settings

_TOKEN: str | None = None
_EXPIRES_AT: float = 0
_LOCK = Lock()


def _base_url() -> str:
    return (
        settings.CURRENCY_CLOUD_LIVE_BASE_URL
        if settings.ENVIRONMENT == "live"
        else settings.CURRENCY_CLOUD_DEV_BASE_URL
    )


def _authenticate() -> str:
    """
    This function returns the token for me to access the currency cloud
    """
    response = requests.post(
        f"{_base_url()}/v2/authenticate/api",
        data={
            "login_id": settings.CURRENCY_CLOUD_LOGIN_ID,
            "api_key": settings.CURRENCY_CLOUD_API_KEY,
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["auth_token"]


def get_auth_token() -> str:
    global _TOKEN, _EXPIRES_AT

    with _LOCK:
        if _TOKEN and time.time() < _EXPIRES_AT:
            return _TOKEN

        _TOKEN = _authenticate()
        _EXPIRES_AT = time.time() + (25 * 60)  # safe TTL

        return _TOKEN


def auth_headers(token: str) -> dict:
    return {"X-Auth-Token": token}


def close_session():
    if not _TOKEN:
        return
    requests.post(
        f"{_base_url()}/v2/authenticate/close_session",
        headers=auth_headers(_TOKEN),
        timeout=5,
    )
