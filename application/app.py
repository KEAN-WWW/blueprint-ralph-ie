from flask import Flask
from application.bp.homepage.routes import homepage

def init_app():
    app = Flask(__name__)
    app.register_blueprint(homepage)
    return app

app = init_app()

if __name__ == "__main__":
    app.run(debug=True)
