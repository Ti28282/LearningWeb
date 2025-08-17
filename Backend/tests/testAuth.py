from fastapi.testclient import TestClient
from Backend.auth.main import app


HTTP_URL = "127.0.0.1:5010/api/v0/"
REGISTER_ENDPOINT = "/register_user"

clinet = TestClient(app)





def test_register_user():
    response = clinet.get(HTTP_URL + REGISTER_ENDPOINT)
    
    assert response.status_code == 200
    assert response.json().get("success") != None
    assert response.json().get("email") != None
    assert response.json().get("create_at") != None



