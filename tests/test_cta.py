from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_cta_stations_returns_list():
    response = client.get("/api/v1/cta/stations")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
