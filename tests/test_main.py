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

    assert response.status_code == 200
    assert response.json() == res_payload


def test_sub():
    payload = {
        "left": 5,
        "right": 20,
    }

    res_payload = {
        "status": 200,
        "message": "successful",
        "result": -15
    }

    response = client.post("/sub", json=payload)

    assert response.status_code == 200
    assert response.json() == res_payload


def test_multiply():
    payload = {
        "left": 5,
        "right": 20,
    }

    res_payload = {
        "status": 200,
        "message": "successful",
        "result": 100
    }

    response = client.post("/multiply", json=payload)

    assert response.status_code == 200
    assert response.json() == res_payload


def test_divide():
    payload = {
        "left": 5,
        "right": 20,
    }

    res_payload = {
        "status": 200,
        "message": "successful",
        "result": 0.25
    }

    response = client.post("/divide", json=payload)

    assert response.status_code == 200
    assert response.json() == res_payload
