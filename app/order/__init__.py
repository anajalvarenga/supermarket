from flask import Blueprint # type: ignore

bp = Blueprint('order', __name__)


from app.order import routes