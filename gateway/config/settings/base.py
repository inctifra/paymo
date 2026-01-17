from collections.abc import Callable
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from datetime import timedelta
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pydantic import computed_field
from pydantic_core import MultiHostUrl
from pydantic.networks import RedisDsn

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
    # Db
    WISE_DATABASE_URI: str = ""
    DEVELOPER_DATABASE_URI: str = ""

    @computed_field
    @property
    def WISE_DATABASE_URL(self)->str:
        return MultiHostUrl(url=self.WISE_DATABASE_URI).unicode_string()

    @computed_field
    @property
    def DEVELOPER_DATABASE_URL(self)->str:
        return MultiHostUrl(url=self.DEVELOPER_DATABASE_URI).unicode_string()

    @computed_field()
    @property
    def ACCESS_TOKEN_EXPIRE(self) -> timedelta:
        return timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
    @computed_field()
    @property
    def REFRESH_TOKEN_EXPIRE(self) -> timedelta:
        return timedelta(minutes=self.REFRESH_TOKEN_EXPIRE_DAYS)

    @computed_field()
    @property
    def REDIS_URL(self)-> str:
        return self.REDIS_URI

settings = Settings()

TORTOISE_ORM = {
    "connections": {"default": settings.WISE_DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.index", "aerich.models"],
            "default_connection": "default",
        },
    },
}