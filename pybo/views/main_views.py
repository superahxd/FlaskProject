from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.model import Question

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/hello")
def hello():
    return "Hi bye"


@bp.route("/")
def index():
    return redirect(url_for("question._list"))
