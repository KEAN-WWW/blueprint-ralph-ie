from flask import Blueprint

bp = Blueprint("bp", __name__)

@bp.route("/hello")
def hello():
    return "Hello from blueprint!"

