from flask import render_template # type: ignore
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')