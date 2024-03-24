import pytest
from app import create_app

@pytest.fixture
def app():
    app=create_app()
    app.config.from_object('config.Testing')
    yield app


@pytest.fixture
def client(app):
    return app.test_client()