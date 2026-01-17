from collections.abc import Callable
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
    )

    # Currencycloud
    CURRENCY_CLOUD_DEV_BASE_URL: str
    CURRENCY_CLOUD_LIVE_BASE_URL: str
    CURRENCY_CLOUD_LOGIN_ID: str
    CURRENCY_CLOUD_API_KEY: str

    # App
    APP_NAME: str = "Paymo"
    ENVIRONMENT: str = "dev"  # dev | live


settings = Settings()
