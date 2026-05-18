from pydantic import BaseModel


class InspectionResult(BaseModel):
    inspection_id: int
    name: str
    aka_name: str | None = None
    license: str | None = None
    facility_type: str | None = None
    address: str | None = None
    zip_code: str | None = None
    risk: str | None = None
    results: str | None = None
    inspection_date: str | None = None
    inspection_type: str | None = None
    violations: str | None = None
