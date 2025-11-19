from application.app import app

def test_blueprint_register():
    assert "homepage" in app.blueprints
