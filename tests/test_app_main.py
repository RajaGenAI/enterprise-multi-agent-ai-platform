from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_and_health_routes_return_200():
    root_response = client.get("/")
    health_response = client.get("/api/v1/health")

    assert root_response.status_code == 200
    assert health_response.status_code == 200
