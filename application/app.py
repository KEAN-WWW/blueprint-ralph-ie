from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the blueprint from application.bp
    from application.bp import bp
    app.register_blueprint(bp)

    return app
