from fastapi.testclient import TestClient
from api.main import app

HTTP_URL = "127.0.0.1:5010/api/v0"

REGISTER = "/register"
TEST = "/test"


client = TestClient(app)



def test_register_user():
    response = client.get(HTTP_URL + REGISTER)
    
    assert response.status_code == 200




def test_endpoint():
    resp = client.get(HTTP_URL + TEST)

    assert resp.status_code == 200

    assert resp.json() in {"status":"OK"}
