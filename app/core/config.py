from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Chicago Smart City API"
    app_version: str = "0.1.0"
    app_prefix: str = "/api/v1"
    food_inspections_url: str = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
