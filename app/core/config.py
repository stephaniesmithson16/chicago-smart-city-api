from functools import lru_cache
from os import getenv

from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Chicago Smart City API"
    environment: str = "local"
    debug: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings(
        environment=getenv("ENVIRONMENT", "local"),
        debug=getenv("DEBUG", "false").lower() == "true",
    )
