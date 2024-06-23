from flask import request # type: ignore
from app.order import bp
from app.extensions import db
from app.models.order import Order
from app.models.order_product import OrderProduct
from app.extensions import db
from app.views.base import format_list, format_single

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        data = request.json
        new_order = Order(customer_id=data.get('customer_id'),
                        employee_id=data.get('employee_id'),)
        db.session.add(new_order)
        db.session.commit()
        
        for product in data.get('products'):
            new_order_product = OrderProduct(order_id=new_order.id, product_id=product)
            db.session.add(new_order_product)
        db.session.commit()

        return format_single(new_order)
    
    orders = Order.query.all()
    return format_list(orders)

@bp.route('/<int:product_id>')
def get_by_id(product_id):
    order = Order.query.filter_by(id=product_id).first()
    return format_single(order)