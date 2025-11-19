from application.app import Flask
from application.bp.homepage.routes import homepage

app = Flask(__name__)

app.register_blueprint(homepage)