from pydantic import BaseModel


class InspectionResult(BaseModel):
    inspection_id: int
    name: str
    aka_name: str
    license: str
    facility_type: str
    address: str
    zip: str
    risk: str
    results: str
    inspection_date: str
    inspection_type: str
    violations: str | None = None
