from flask import Blueprint # type: ignore

bp = Blueprint('customer', __name__)

from app.customer import routes