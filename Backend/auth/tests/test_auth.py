from fastapi.testclient import TestClient
from Backend.auth.app.main import app
import pytest

HTTP_URL = "127.0.0.1:5010/api/v0/"
REGISTER_ENDPOINT = "/register"
LOGIN_ENDPOINT = "/login"
EMAIL = "test_root@gmail.com"
LOGIN = "TEST_ROOT"
PASSWORD = "test_root"

client = TestClient(app)


def test_GET_register():
    response = client.get(HTTP_URL + REGISTER_ENDPOINT)
    
    assert response.status_code == 200
    
def test_POST_register():
    json_ = {
        "email":EMAIL,
        "password":PASSWORD,
        "login":LOGIN
    }

    response = client.post(url = HTTP_URL + REGISTER_ENDPOINT, json = json_).json()

    assert response.get("status") == "OK"

    

