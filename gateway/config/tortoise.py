from .settings.base import settings

TORTOISE_ORM = {
    "connections": {
        "default": settings.WISE_DATABASE_URL,
        "developer": settings.DEVELOPER_DATABASE_URL,
    },
    "apps": {
        "wise_models": {
            "models": ["models.wise", "aerich.models"],
            "default_connection": "default",
        },
        "developer_models": {
            "models": ["models.developer"],
            "default_connection": "developer",
        },
    },
}
