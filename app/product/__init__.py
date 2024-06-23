from flask import Blueprint # type: ignore

bp = Blueprint('product', __name__)


from app.product import routes