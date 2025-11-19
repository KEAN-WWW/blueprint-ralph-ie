from flask import Flask
from application.bp import bp   # THIS NOW WORKS

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
