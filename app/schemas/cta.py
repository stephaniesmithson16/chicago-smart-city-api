from pydantic import BaseModel


class CTAStation(BaseModel):
    name: str
    descriptive_name: str
    ada: bool
    line: str | list[str]
    latitude: float
    longitude: float


class TrainArrival(BaseModel):
    station_name: str
    stop_description: str
    route: str
    destination: str
    arrival_time: str
    is_delayed: bool
