import pytest
from fastapi.testclient import TestClient

from main import app

@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "id" in response.json()
    assert "thumbnail" in response.json()
    # Добавьте другие проверки по мере необходимости


def test_read_list(client):
    response = client.get("/list/?q=1,2,3")
    assert response.status_code == 200
    assert isinstance(response.json(), list)