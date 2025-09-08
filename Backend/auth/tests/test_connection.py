from fastapi.testclient import TestClient
from auth import app

clinet = TestClient(app)


def test_read_main():
    response = clinet.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}



