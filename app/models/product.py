from app.extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    quantity = db.Column(db.Integer)
    order_products = db.relationship('OrderProduct', backref='product')

    def __repr__(self):
        return f'<Product "{self.name}">'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}