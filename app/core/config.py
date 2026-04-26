from pydantic import BaseModel


class Settings(BaseModel):
    api_name: str = "Chicago Smart City API"
    api_version: str = "0.1.0"
    api_prefix: str = "/api/v1"


settings = Settings()
