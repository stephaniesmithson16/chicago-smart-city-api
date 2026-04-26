from pydantic import BaseModel


class CTAStation(BaseModel):
    station_id: int
    name: str
    line: str
    neighborhood: str
