from flask import Blueprint # type: ignore

bp = Blueprint('employee', __name__)


from app.employee import routes