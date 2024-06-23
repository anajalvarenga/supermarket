from flask import request # type: ignore
from app.customer import bp
from app.extensions import db
from app.models.customer import Customer
from app.extensions import db
from app.views.base import format_list, format_single

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        new_customer = Customer(name=data.get('name'),
                            address=data.get('address'),
                            phone=data.get('phone'),)
        db.session.add(new_customer)
        db.session.commit()
        return format_single(new_customer)
    
    customers = Customer.query.all()
    return format_list(customers)

@bp.route('/<int:customer_id>')
def get_by_id(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    return format_single(customer)