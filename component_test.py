from fastapi.testclient import TestClient
from main import app

base_url = 'http://localhost:80/'


def test_root_get():
    with TestClient(app) as client:
        response = client.get("/")
        res = response.json()

        assert 'id' in res.keys()
        assert 'description' in res.keys()
        assert isinstance(res['id'], int)


def test_list_route_with_param():
    with TestClient(app) as client:
        response = client.get("/list/?q=1")
        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) > 0

        first_item = data[0] if data else {}

        assert first_item.get('id') == 1
        assert first_item.get('title') == 'Dauntless'
        assert first_item.get('thumbnail') == 'https://www.mmobomb.com/g/1/thumbnail.jpg'
        assert first_item.get('release_date') == '2019-05-21'

# 1
#2