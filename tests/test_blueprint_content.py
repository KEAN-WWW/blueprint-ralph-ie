
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
    """flask unit testing for content in default page"""

# pylint: disable=unused-argument
def test_about_page_content(client):
    """flask unit testing for content in about page"""