from fastapi import FastAPI
from config.settings.base import settings
from contextlib import asynccontextmanager
from services.currencycloud.client import close_session


from routes import currency_cloud_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    close_session()


app = FastAPI(
    title=f"{settings.APP_NAME} Payment Gateway", docs_url="/", lifespan=lifespan
)


app.include_router(
    currency_cloud_router,
    prefix="",
    tags=["Internal – Currencycloud"],
)
