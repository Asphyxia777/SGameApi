import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from main import app

@pytest.fixture
def client():
    return TestClient(app)

@patch('main.random.randint')
@patch('main.requests.get')
def test_root(mock_requests_get, mock_randint, client):
    mock_randint.return_value = 42
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 42, "name": "Test Game"}
    mock_requests_get.return_value = mock_response

    response = client.get("/")
    assert response.status_code == 200
    assert "id" in response.json()
    assert "name" in response.json()
    assert response.json()["id"] == 42
    assert response.json()["name"] == "Test Game"

@patch('main.requests.get')
def test_get_list(mock_requests_get, client):
    mock_response = MagicMock()
    mock_response.json.side_effect = [{"id": 1, "name": "Game 1"}, {"id": 2, "name": "Game 2"}]
    mock_requests_get.side_effect = [mock_response, mock_response]

    response = client.get("/list/?q=1,2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["name"] == "Game 1"
    assert response.json()[1]["id"] == 2
    assert response.json()[1]["name"] == "Game 2"
