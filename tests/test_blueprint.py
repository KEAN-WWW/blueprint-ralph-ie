import pytest
from wsgi import app

@pytest.fixture(name="client")
def create_client():
    with app.test_client() as client:
        yield client

def test_main_page_content(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Blueprint" in response.data

def test_about_page_content(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Blueprint" in response.data
