from flask import request # type: ignore
from app.product import bp
from app.extensions import db
from app.models.product import Product
from app.views.base import format_list, format_single

@bp.route('/', methods=('GET', 'POST', 'OPTIONS'))
def index():
    if request.method == 'OPTIONS':
        response = bp.make_default_options_response()
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response
    
    if request.method == 'POST':
        data = request.json
        new_product = Product(name=data.get('name'),
                        description=data.get('description'),
                        quantity=data.get('quantity'),)
        db.session.add(new_product)
        db.session.commit()
        return format_single(new_product)
    
    products = Product.query.all()
    return format_list(products)

@bp.route('/<int:product_id>')
def get_by_id(product_id):
    product = Product.query.filter_by(id=product_id).first()
    return format_single(product)