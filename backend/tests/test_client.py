import pytest
from flask import Flask
from base64 import b64encode

from app import create_app  # Replace with your actual app module

class TestClient:
    def __init__(self, app, username, password):
        self.app = app
        self.auth = 'Basic ' + b64encode((username + ':' + password)
                                         .encode('utf-8')).decode('utf-8')

    def send(self, url, method='GET', data=None, headers={}):
        with self.app.test_client() as client:
            headers['Authorization'] = self.auth
            if method == 'GET':
                response = client.get(url, headers=headers)
            elif method == 'POST':
                response = client.post(url, json=data, headers=headers)
            elif method == 'PUT':
                response = client.put(url, json=data, headers=headers)
            elif method == 'DELETE':
                response = client.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            return response.status_code, response.json()

    def get(self, url, headers={}):
        return self.send(url, 'GET', headers=headers)

    def post(self, url, data, headers={}):
        return self.send(url, 'POST', data, headers=headers)

    def put(self, url, data, headers={}):
        return self.send(url, 'PUT', data, headers=headers)

    def delete(self, url, headers={}):
        return self.send(url, 'DELETE', headers=headers)

@pytest.fixture
def app():
    """Create and configure a test app instance."""
    app = create_app('test')  # Assuming 'test' is the name of your test configuration
    yield app

@pytest.fixture
def client(app):
    """Create a test client."""
    return TestClient(app, 'username', 'password')

def test_get(client):
    """Test the GET request."""
    # Example test for GET request
    rv, data = client.get('/api/endpoint')
    assert rv == 200
    assert 'key' in data

def test_post(client):
    """Test the POST request."""
    # Example test for POST request
    data = {'key': 'value'}
    rv, data = client.post('/api/endpoint', data)
    assert rv == 201
    assert 'id' in data

# Add more test functions for other HTTP methods as needed
