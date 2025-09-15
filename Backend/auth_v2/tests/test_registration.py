from fastapi.testclient import TestClient
from api.main import app

HTTP_URL = "127.0.0.1:5010/api/v0"

REGISTER = "/register"
TEST = "/test"
LOGIN = "/login"

EMAIL = "test_root@gmail.com"
PASSWORD = "test_root"
LOGIN = "TEST_ROOT"

client = TestClient(app)



def test_GET_register():
    response = client.get(HTTP_URL + REGISTER)
    
    assert response.status_code == 200

def test_POST_register():
    json_ = {
        "email":EMAIL,
        "login":LOGIN,
        "password":PASSWORD
    }
    response = client.get(url = HTTP_URL + LOGIN, json = json_).json()

    assert response.get("status") == "OK"



def test_endpoint():
    resp = client.get(HTTP_URL + TEST)

    assert resp.status_code == 200

    assert resp.json() in {"status":"OK"}






