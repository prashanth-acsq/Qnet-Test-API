from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"statusCode": 200, "statusText": "Root Page"}


def test_wakeup():
    response = client.get("/wakeup")
    assert response.status_code == 200
    assert response.json() == {"statusCode": 200, "statusText": "Awake"}

