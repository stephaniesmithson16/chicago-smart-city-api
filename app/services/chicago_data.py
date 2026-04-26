import httpx

URL = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"


def get_high_risk_restaurants(limit: int = 10) -> list[dict]:
    params = {
        "$limit": limit,
        "$where": "risk = 'Risk 1 (High)'",
        "$order": "inspection_date DESC",
    }

    response = httpx.get(URL, params=params, timeout=10.0)
    response.raise_for_status()

    return response.json()
