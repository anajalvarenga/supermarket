from app.extensions import db
from app.models.product import Product

class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return f'<OrderProduct "{self.id}">'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}