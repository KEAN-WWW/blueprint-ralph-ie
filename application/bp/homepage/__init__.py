from flask import Flask
from .routes import bp  # replace with your actual blueprint file

# create the Flask app
app = Flask(__name__)

# register your blueprint
app.register_blueprint(bp)
