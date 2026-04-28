from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Chicago Smart City API"
    app_version: str = "0.1.0"
    app_prefix: str = "/api/v1"

    food_inspections_url: str = (
        "https://data.cityofchicago.org/resource/4ijn-s7e5.json"
    )

    cta_train_tracker_api_key: str | None = None
    cta_train_arrivals_url: str = (
        "https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    )
    cta_stations_url: str = (
        "https://data.cityofchicago.org/resource/8mj8-j3c4.json"
    )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


settings = Settings()
