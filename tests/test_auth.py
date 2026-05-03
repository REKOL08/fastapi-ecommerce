import os
os.environ["APP_ENV"] = "testing"
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from app.db.session import Base, get_db

# Base de datos SQLite en memoria para tests
SQLALCHEMY_TEST_URL = "sqlite:///./test.db"
engine_test = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine_test)

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine_test)
    Base.metadata.create_all(bind=engine_test)
    yield


def test_register_user():
    response = client.post("/api/v1/auth/register", json={
        "name": "Juan Pérez",
        "email": "juan@test.com",
        "password": "segura123",
    })
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "juan@test.com"
    assert data["role"] == "customer"


def test_register_duplicate_email():
    payload = {"name": "Ana", "email": "ana@test.com", "password": "pass1234"}
    client.post("/api/v1/auth/register", json=payload)
    r = client.post("/api/v1/auth/register", json=payload)
    assert r.status_code == 409


def test_login_success():
    client.post("/api/v1/auth/register", json={
        "name": "Carlos", "email": "carlos@test.com", "password": "mipass99"
    })
    r = client.post("/api/v1/auth/login", json={
        "email": "carlos@test.com", "password": "mipass99"
    })
    assert r.status_code == 200
    assert "access_token" in r.json()


def test_login_wrong_password():
    client.post("/api/v1/auth/register", json={
        "name": "Luis", "email": "luis@test.com", "password": "correcta1"
    })
    r = client.post("/api/v1/auth/login", json={
        "email": "luis@test.com", "password": "incorrecta"
    })
    assert r.status_code == 401


def test_get_me():
    client.post("/api/v1/auth/register", json={
        "name": "María", "email": "maria@test.com", "password": "pass1234"
    })
    login = client.post("/api/v1/auth/login", json={
        "email": "maria@test.com", "password": "pass1234"
    })
    token = login.json()["access_token"]
    r = client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["email"] == "maria@test.com"
