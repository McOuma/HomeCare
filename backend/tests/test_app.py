import pytest
from werkzeug.exceptions import NotFound
from app import create_app
from app.models import User
from .test_client import TestClient

@pytest.fixture
def app():
    from app import db
    """Create and configure a test app instance."""
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        u = User(username='mugah')
        u.set_password('cat')
        db.session.add(u)
        db.session.commit()
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create a test client."""
    with app.test_client() as client:
        yield client

def test_user(client):
    # Assuming you have an endpoint for fetching user details
    # Here's a sample implementation for testing the user endpoint
    rv = client.get('/api/v1/user')  # Assuming '/api/v1/user' is the endpoint
    assert rv.status_code == 200
    assert 'username' in rv.json  # Assuming the response contains the username

def test_booking(client):
    # Assuming you have an endpoint for managing bookings
    # Here's a sample implementation for testing the booking endpoint
    rv = client.post('/api/v1/booking', json={'date': '2024-03-26'})  # Assuming '/api/v1/booking' is the endpoint
    assert rv.status_code == 201
    assert 'id' in rv.json  # Assuming the response contains the booking ID

def test_caregiver(client):
    # Assuming you have an endpoint for managing caregivers
    # Here's a sample implementation for testing the caregiver endpoint
    rv = client.get('/api/v1/caregiver')  # Assuming '/api/v1/caregiver' is the endpoint
    assert rv.status_code == 200
    assert 'name' in rv.json  # Assuming the response contains the caregiver's name

def test_pagination(client):
    # Assuming you have an endpoint with pagination support
    # Here's a sample implementation for testing pagination
    rv = client.get('/api/v1/items?page=1&limit=10')  # Assuming '/api/v1/items' supports pagination
    assert rv.status_code == 200
    assert 'items' in rv.json  # Assuming the response contains the paginated items
