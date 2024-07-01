from flask import request # type: ignore
from flask_cors import cross_origin

from app.models.product import Product
from app.order import bp
from app.extensions import db
from app.models.order import Order
from app.models.order_product import OrderProduct
from app.extensions import db
from app.views.base import format_list, format_single

@bp.route('/', methods=('GET', 'POST', 'OPTIONS'))
@cross_origin()
def index():
    if request.method == 'OPTIONS':
        response = bp.make_default_options_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response
    
    if request.method == 'POST':
        data = request.json
        new_order = Order(customer_id=data.get('customer_id'),
                        employee_id=data.get('employee_id'),)
        db.session.add(new_order)
        db.session.commit()
        
        for product_sale in data.get('products'):
            stock_product = Product.query.filter_by(id=product_sale['id']).first()

            if stock_product.quantity > int(product_sale['buy']):
                setattr(stock_product, 'quantity', stock_product.quantity - int(product_sale['buy']))

                new_order_product = OrderProduct(order_id=new_order.id, product_id=stock_product.id)
                db.session.add(new_order_product)
        db.session.commit()

        return format_single(new_order)
    
    orders = Order.query.all()
    return format_list(orders)

@bp.route('/<int:product_id>')
def get_by_id(product_id):
    order = Order.query.filter_by(id=product_id).first()
    return format_single(order)