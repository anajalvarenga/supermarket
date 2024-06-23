import random

from app.extensions import db
from app.models.customer import Customer
from app.models.employee import Employee
from app.models.order_product import OrderProduct
from app.models.order import Order
from app.models.product import Product

db.create_all()

for i in range(0, 5):
    random_num = random.randrange(1, 1000)
    customer = Customer(name=f"Customer #{random_num}",
                        address="UNIFEI",
                        phone="35999999999",)
    db.session.add(customer)
    print(customer)
    print(customer.name)
    print('--')
    db.session.commit()

for i in range(0, 5):
    random_num = random.randrange(1, 1000)
    employee = Employee(name=f"Employee #{random_num}",
                        address="Mercadinho local",
                        phone="35999999999",)
    db.session.add(employee)
    print(employee)
    print(employee.name)
    print('--')
    db.session.commit()

random_num = random.randrange(1, 1000)
product = Product(name="Pão",
                    description="pão superfaturado",
                    quantity=20,)
db.session.add(product)
print(product)
print(product.name)
print('--')
db.session.commit()

random_num = random.randrange(1, 1000)
product = Product(name="Refrigerante",
                    description="coquinha gelada",
                    quantity=10,)
db.session.add(product)
print(product)
print(product.name)
print('--')
db.session.commit()

random_num = random.randrange(1, 1000)
product = Product(name="Cerveja",
                    description="petra de caminhão capotado",
                    quantity=100,)
db.session.add(product)
print(product)
print(product.name)
print('--')
db.session.commit()

random_num = random.randrange(1, 1000)
order = Order(customer_id=1, employee_id=1,)
db.session.add(order)
print(order)
print('--')
db.session.commit()

for product in [1, 2, 3]:
    new_order_product = OrderProduct(order_id=1, product_id=product)
    db.session.add(new_order_product)
db.session.commit()