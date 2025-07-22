from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..app.main import app
from ..app.db.database import get_db, Base
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def auth_headers():
    user = {"email": "budgetuser@example.com", "password": "password"}
    client.post("/auth/register", json=user)
    response = client.post("/auth/login", data={"username": user["email"], "password": user["password"]})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_budget(auth_headers):
    response = client.post(
        "/budgets/",
        json={"name": "Groceries", "allocated_amount": 500.0},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Groceries"
    assert response.json()["allocated_amount"] == 500.0

def test_get_budgets(auth_headers):
    response = client.get("/budgets/", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
