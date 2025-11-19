from flask import Blueprint

bp = Blueprint("bp", __name__)

@bp.route("/")
def index():
    return "Blueprint Home Page"

@bp.route("/about")
def about():
    return "Blueprint About Page"
