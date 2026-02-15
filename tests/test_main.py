from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_sum():
    payload = {
        "left": 5,
        "right": 20,
    }

    res_payload = {
        "status": 200,
        "message": "successful",
        "result": 25
    }

    response = client.post("/sum", json=payload)
    print(response)

    assert response.status_code == 200
    assert response.json() == res_payload
