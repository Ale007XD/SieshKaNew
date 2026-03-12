# app/core/config.py

from pydantic import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Sieshka API"

    DATABASE_URL: str = "sqlite:///./app.db"

    API_PREFIX: str = "/api"

    DEBUG: bool = True


settings = Settings()
