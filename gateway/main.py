from fastapi import FastAPI
from config.settings.base import settings
from contextlib import asynccontextmanager
from services.currencycloud.client import close_session

from config.tortoise import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise
from routes import currency_cloud_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    close_session()


app = FastAPI(
    title=f"{settings.APP_NAME} Payment Gateway", docs_url="/", lifespan=lifespan
)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(
    currency_cloud_router,
    prefix="",
    tags=["Internal – Currencycloud"],
)
