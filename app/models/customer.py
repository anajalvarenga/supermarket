from app.extensions import db
from app.models.order import Order

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(250))
    phone = db.Column(db.String(11))
    orders = db.relationship('Order', backref='customer')

    def __repr__(self):
        return f'<Customer "{self.name}">'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}