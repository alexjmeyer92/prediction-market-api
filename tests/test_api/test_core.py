from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "This is the prediction market api"}


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"message": "Prediction Market API is running and healthy"}
