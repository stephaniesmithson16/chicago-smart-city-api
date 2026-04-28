from app.schemas.cta import CTAStation, TrainArrival

CTA_LINES = {
    "Red": "red",
    "Blue": "blue",
    "Green": "g",
    "Brown": "brn",
    "Purple": "p",
    "Yellow": "y",
    "Pink": "pnk",
    "Orange": "o",
}


def parse_station_lines(data: dict) -> list[str]:
    lines = []
    for line_name, key in CTA_LINES.items():
        if data.get(key, False):
            lines.append(line_name)
    return lines


def map_cta_stations(data: dict) -> CTAStation:
    coordinates = data.get("location", {}).get("coordinates", [0.0, 0.0])

    return CTAStation(
        name=data.get("station_name", "Unknown"),
        descriptive_name=data.get("station_descriptive_name", "Unknown"),
        ada=data.get("ada", False),
        line=parse_station_lines(data),
        latitude=coordinates[0],
        longitude=coordinates[1],
    )


def map_train_arrival(data: dict) -> TrainArrival:
    return TrainArrival(
        station_name=data.get("staNm", "Unknown"),
        stop_description=data.get("stpDe", "Unknown"),
        route=data.get("rt", "Unknown"),
        destination=data.get("destNm", "Unknown"),
        arrival_time=data.get("arrT", "Unknown"),
        is_delayed=data.get("isApp", "0") == "1",
    )
