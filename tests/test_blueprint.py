"""This is a test script to test flask application"""
import pytest
from wsgi import app

@pytest.fixture(name="client")
def create_client():
    """Test if there is blueprint registered"""
    with app.test_client() as client:
        yield client  # ✅ correct

# pylint: disable=unused-argument
def test_main_page_content(client):
    """Test that the home page loads and has Blueprint"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'Blueprint' in response.data

# pylint: disable=unused-argument
def test_about_page_content(client):
    """Tests thatthe about page loads and has Blueprint"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b'Blueprint' in response.data