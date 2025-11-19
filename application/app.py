from flask import Flask
from application.bp.homepage.routes import homepage  # ← NEW

app = Flask(__name__)

app.register_blueprint(homepage)         # ← NEW

if __name__ == '__main__':
    app.run(debug=True)
# your existing routes...