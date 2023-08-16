from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "statusCode": 200,
        "statusText" : "Root Endpoint of Q-net Test API"
    }


def test_get_random():
    response = client.get("/random")
    assert response.status_code == 200
    assert response.json() == {
        "statusCode" : 200,
        "statusText" : "Random Data Generation Endpoint of Q-net Test API"
    }
