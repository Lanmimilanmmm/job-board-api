from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Job Board API radi!"}

def test_create_job_unauthorized():
    response = client.post("/jobs/", json={
        "title": "Python Developer",
        "company": "Test Firma",
        "location": "Niš",
        "tech_stack": "Python, FastAPI",
        "description": "Test oglas"
    })
    assert response.status_code == 401

def test_register_user():
    response = client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"

def test_login_user():
    response = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "test123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_job_authorized():
    # Login
    login = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "test123"
    })
    token = login.json()["access_token"]

    # Dodaj oglas sa tokenom
    response = client.post("/jobs/", 
        json={
            "title": "Python Developer",
            "company": "Test Firma",
            "location": "Niš",
            "tech_stack": "Python, FastAPI",
            "description": "Test oglas"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Python Developer"

def test_get_jobs():
    response = client.get("/jobs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_search_jobs():
    response = client.get("/jobs/?tech=Python")
    assert response.status_code == 200