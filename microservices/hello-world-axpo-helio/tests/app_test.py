import pytest

# https://github.com/pallets/flask/blob/master/examples/tutorial/tests/conftest.py

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    from hello_world_axpo_helio.app import app
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_hello_world_items(client):
    """Start with a blank database."""

    rv = client.get('/helloworld/items/')
    assert b'No entries here so far' in rv.data
