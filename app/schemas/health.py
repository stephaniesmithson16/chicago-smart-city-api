from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str
    app: str
    environment: str
