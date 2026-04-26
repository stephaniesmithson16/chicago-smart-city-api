from pydantic import BaseModel


class InspectionResult(BaseModel):
    name: str
    address: str
    risk: str
    results: str
    inspection_date: str
    violations: str | None = None
