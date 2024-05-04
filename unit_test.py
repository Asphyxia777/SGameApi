import unittest
from unittest.mock import patch
from starlette.testclient import TestClient
from main import app, root, get_list
import httpx

class TestApp(unittest.TestCase):

    @patch('main.requests.get')
    def test_root(self, mock_get):
        mock_get.return_value.json.return_value = {"game": "test_game"}
        client = TestClient(app)
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"game": "test_game"})

    @patch('main.requests.get')
    def test_get_list(self, mock_get):
        mock_get.return_value.json.return_value = {"game": "test_game"}
        client = TestClient(app)
        response = client.get('/list/?q=[1]')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"game": "test_game"}])

if __name__ == '__main__':
    unittest.main()