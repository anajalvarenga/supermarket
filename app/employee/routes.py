from flask import request # type: ignore
from app.employee import bp
from app.extensions import db
from app.models.employee import Employee
from app.extensions import db
from app.views.base import format_list, format_single

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        new_employee = Employee(name=data.get('name'),
                            address=data.get('address'),
                            phone=data.get('phone'),)
        db.session.add(new_employee)
        db.session.commit()
        return format_single(new_employee)
    
    employees = Employee.query.all()
    return format_list(employees)

@bp.route('/<int:employee_id>')
def get_by_id(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    return format_single(employee)