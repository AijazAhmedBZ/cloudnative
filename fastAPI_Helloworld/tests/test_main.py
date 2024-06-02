from fastapi.testclient import TestClient
from fastapi_helloworld.main import app

def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_piaic_description():
    client = TestClient(app=app)
    response = client.get("/piaic")
    assert response.status_code == 200
    assert response.json() == {"organization": "PIAIC"}

def test_third_check():
    client = TestClient(app=app)
    response = client.get("/piaic")
    assert response.status_code == 200
    assert response.json() == {"organization": "ABC"}