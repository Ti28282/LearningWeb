from fastapi.testclient import TestClient
from Backend.auth.app.main import app
import pytest

HTTP_URL = "127.0.0.1:5010/api/v0/"
REGISTER_ENDPOINT = "/register_user"

client = TestClient(app)


def test_register_user():
    response = client.get(HTTP_URL + REGISTER_ENDPOINT)
    
    assert response.status_code == 200
    


