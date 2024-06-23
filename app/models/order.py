from app.extensions import db
from app.models.order_product import OrderProduct
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    order_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    order_products = db.relationship('OrderProduct', backref='order')

    def __repr__(self):
        return f'<Order "{self.id}">'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}